import math
import os
import traci
from traci import exceptions

from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.simulation.simulation_engine.arbitration import \
    Arbitration
from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.simulation.simulation_engine.vehicle import Vehicle
from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.config import SUMO_HOME, SUMO_BINARY, SUMO_CFG_FILE, \
    SUMO_OPTIONS, TIME_STEP, SIMULATION_END, SUMO_CONFIG_ROOT, TIME_TO_COLLISION, DELTA, LEADER_STARTING_SPEED, LEADER_ENDING_SPEED, STOP_AND_GO_GENERATION_TIME


class Simulator:
    def __init__(self):
        self.sumo_home = SUMO_HOME
        self.sumo_binary = SUMO_BINARY
        self.sumo_cfg_file = SUMO_CFG_FILE
        self.sumo_options = SUMO_OPTIONS
        self.time_step = TIME_STEP

    def open_TraCI_connection(self):
        sumo_cmd = [os.path.join(self.sumo_home, self.sumo_binary), '-c',
                    os.path.join(SUMO_CONFIG_ROOT, self.sumo_cfg_file)]
        sumo_cmd.extend([str(item) for pair in self.sumo_options.items() for item in pair if item is not None])
        traci.start(sumo_cmd)
        print("TraCI connection opened.")

    @staticmethod
    def close_TraCI_connection():
        traci.close()
        print("TraCI connection closed.")

    def run_simulation(self):
        vehicles_dict = {}
        time_step = -1
        try:
            while time_step < SIMULATION_END:
                traci.simulationStep()
                time_step += 1
                for veh_id in traci.vehicle.getIDList():
                    if veh_id not in vehicles_dict.keys():
                        vehicles_dict[veh_id] = Vehicle(veh_id, traci.vehicle.getTypeID(veh_id))
                    vehicle = vehicles_dict[veh_id]
                    # traci.vehicle.setSpeedMode(veh_id, 32)
                    # traci.vehicle.setSpeed(veh_id, 20.0)
                    vehicle_data = self.collect_vehicle_data(time_step, veh_id)
                    self.store_vehicle_data(vehicle, vehicle_data)
                    print(f"  Simulation step {time_step} completed.")
                try:
                    # if time_step <= STOP_AND_GO_GENERATION_TIME:
                    #     traci.vehicle.setSpeed("veh00", LEADER_STARTING_SPEED)
                    # if time_step > STOP_AND_GO_GENERATION_TIME:
                    #     traci.vehicle.setSpeed("veh00", LEADER_ENDING_SPEED)
                    # if time_step == STOP_AND_GO_GENERATION_TIME:
                    #     traci.vehicle.setAcceleration("veh00", -2, 20)
                    pass
                except:
                    pass

        except traci.exceptions.TraCIException:
            raise traci.exceptions.TraCIException
        else:
            print("No exceptions raised")
        finally:
            print("Simulation completed.")
            return vehicles_dict

    @staticmethod
    def store_vehicle_data(vehicle, vehicle_data):
        vehicle.time.append(vehicle_data['time'])
        vehicle.x_position.append(vehicle_data['position'])
        vehicle.speed.append(vehicle_data['speed'])
        vehicle.acceleration.append(vehicle_data['acceleration'])
        vehicle.distance_pred.append(vehicle_data['predecessor_distance'])
        vehicle.timegap_pred.append(vehicle_data['time_gap'])
        vehicle.speed_difference_pred.append(vehicle_data['speed_difference'])
        vehicle.arbitration.append(vehicle_data['arbitration'])
        print(f"    Stored data for vehicle '{vehicle.id}' at time {vehicle_data['time']}.")

    def collect_vehicle_data(self, time_step, veh_id):
        x_position = traci.vehicle.getPosition(veh_id)[0]
        y_position = traci.vehicle.getPosition(veh_id)[1]
        speed = traci.vehicle.getSpeed(veh_id)
        acceleration = traci.vehicle.getAcceleration(veh_id)
        leader_id = "veh" + str((int(veh_id[3:]) - 1) % traci.vehicle.getIDCount()).zfill(2)
        distance_pred = self.distance_from_leader(leader_id, x_position, y_position) \
                        - traci.vehicle.getLength(veh_id) \
                        - traci.vehicle.getMinGap(veh_id)
        pred_speed = traci.vehicle.getSpeed(leader_id)
        speed_difference_pred = pred_speed - speed
        # if traci.vehicle.getLeader(veh_id) is not None:
        #     leader_id, distance = traci.vehicle.getLeader(veh_id)
        #     distance_pred = math.sqrt(math.pow(x_position - traci.vehicle.getPosition(leader_id)[0], 2) + math.pow(y_position - traci.vehicle.getPosition(leader_id)[1], 2)) - 5.0
        #     pred_speed = traci.vehicle.getSpeed(leader_id)
        #     speed_difference_pred = pred_speed - speed
        # else:
        #     leader_id = "veh" + str((int(veh_id[3:]) - 1) % traci.simulation.getIDCount()).zfill(2)
        #     distance_pred = math.sqrt(math.pow(x_position - traci.vehicle.getPosition(leader_id)[0], 2) + math.pow(
        #         y_position - traci.vehicle.getPosition(leader_id)[1], 2)) - 5.0
        #     pred_speed = traci.vehicle.getSpeed(leader_id)
        #     speed_difference_pred = pred_speed - speed
            # except:
            #     distance_pred = float('inf')
            #     speed_difference_pred = float('inf')
        try:
            timegap_pred = distance_pred / speed
        except ZeroDivisionError:
            timegap_pred = float('inf')
        arbitration = Arbitration(TIME_TO_COLLISION, DELTA)
        sharing = arbitration.compute_sharing_value(timegap_pred)
        vehicle_data = {
            'time': time_step,
            'position': x_position,
            'speed': speed,
            'acceleration': acceleration,
            'predecessor_distance': distance_pred,
            'time_gap': timegap_pred,
            'speed_difference': speed_difference_pred,
            'arbitration': sharing
        }
        print(f"    Collected data for vehicle '{veh_id}' at time {time_step}.")
        return vehicle_data

    @staticmethod
    def distance_from_leader(leader_id, x_position, y_position):
        return math.sqrt(math.pow(x_position - traci.vehicle.getPosition(leader_id)[0], 2) + math.pow(
            y_position - traci.vehicle.getPosition(leader_id)[1], 2))
