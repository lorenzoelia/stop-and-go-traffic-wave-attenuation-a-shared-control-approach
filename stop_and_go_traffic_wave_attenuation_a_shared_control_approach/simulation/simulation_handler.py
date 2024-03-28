import os
from datetime import datetime

from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.simulation.simulation_engine.simulator import \
    Simulator
from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.simulation.simulation_engine.data_saver import DataSaver
from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.config import MONTECARLO_ITERATIONS, \
    SIMULATIONS_ROOT, ACC_PENETRATION_PERCENTAGE_SPLITS, IDM_PENETRATION_PERCENTAGE_SPLITS, \
    SHC_PENETRATION_PERCENTAGE_SPLITS


class SimulationHandler:
    def __init__(self):
        self.num_montecarlo_simulations = MONTECARLO_ITERATIONS
        self.simulator = Simulator()
        self.simulations_folder = None
        self.create_simulations_folder()

    def montecarlo_simulation(self, save_results_folder):
        print("Starting Monte Carlo simulation...")
        for iteration in range(self.num_montecarlo_simulations):
            iteration_folder = self.create_iteration_folder(iteration, save_results_folder)
            self.simulator.open_TraCI_connection()
            microscopic_results_dict = self.simulator.run_simulation()
            self.simulator.close_TraCI_connection()
            self.save_vehicles_data(microscopic_results_dict, iteration_folder)
            print("Monte Carlo simulation completed.")

    def create_iteration_folder(self, iteration, save_results_folder):
        iteration_folder = os.path.join(save_results_folder, f"sim_{iteration}_{datetime.now().strftime('%H%M%S')}")
        os.makedirs(iteration_folder)
        print(f"    Iteration {iteration + 1}/{self.num_montecarlo_simulations}: Created folder '{iteration_folder}'")
        return iteration_folder

    def create_simulations_folder(self):
        self.simulations_folder = os.path.join(SIMULATIONS_ROOT, datetime.now().strftime('%Y%m%d_%H%M%S'))
        os.makedirs(self.simulations_folder)
        print(f"Created simulations folder: '{self.simulations_folder}'")

    def save_vehicles_data(self, microscopic_results_dict, save_results_folder):
        for veh_id in microscopic_results_dict.keys():
            DataSaver.export_vehicle_to_csv(microscopic_results_dict[veh_id], save_results_folder)
            print(f"    Saved data for vehicle '{veh_id}' in '{save_results_folder}'")
