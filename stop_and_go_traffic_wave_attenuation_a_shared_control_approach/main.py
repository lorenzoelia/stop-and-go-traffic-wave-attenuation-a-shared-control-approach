import os.path

from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.preprocessing.XML_to_CSV_converter import \
    XMLToCSVConverter
from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.simulation.simulation_handler import \
    SimulationHandler
from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.processing.sensitivity_analysis import \
    SensitivityAnalysis
from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.data_prep.demand_generator import DemandGenerator
from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.config import SUMO_CONFIG_ROOT, SUMO_ROUTE_FILE, NUM_VEHICLES_PER_ROUTE, NUM_ROUTES, LEADER_STARTING_SPEED


def main():
    # Prepare route file
    demand_generator = DemandGenerator(os.path.join(SUMO_CONFIG_ROOT, SUMO_ROUTE_FILE))
    demand_generator.set_density(NUM_ROUTES, NUM_VEHICLES_PER_ROUTE, LEADER_STARTING_SPEED)

    # Instantiate simulator handler
    simulation_handler = SimulationHandler()

    # Pre-process the route file to save the configuration in this run
    converter = XMLToCSVConverter(os.path.join(SUMO_CONFIG_ROOT, SUMO_ROUTE_FILE))
    converter.convert_to_csv(os.path.join(simulation_handler.simulations_folder, 'parameters.csv'))
    print("Pre-processing completed. Starting sensitivity analysis...")

    # Prepare for sensitivity analysis
    sensitivity_analysis = SensitivityAnalysis(simulation_handler)

    # Run multiple simulations
    sensitivity_analysis.sensitivity_combinations_simulation()
    print("Sensitivity analysis completed. Exiting program.")


if __name__ == '__main__':
    main()
