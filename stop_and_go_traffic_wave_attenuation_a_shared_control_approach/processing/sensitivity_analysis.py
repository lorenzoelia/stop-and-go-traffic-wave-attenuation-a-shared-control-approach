import os

from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.config import ACC_PENETRATION_PERCENTAGE_SPLITS, \
    IDM_PENETRATION_PERCENTAGE_SPLITS, SHC_PENETRATION_PERCENTAGE_SPLITS, SUMO_CONFIG_ROOT, SUMO_ROUTE_FILE, SIMULATIONS_ROOT
from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.data_prep.XML_file_editor import XMLFileEditor


class SensitivityAnalysis:
    def __init__(self, simulation_handler):
        self.simulation_handler = simulation_handler
        self.sumo_route_file = os.path.join(SUMO_CONFIG_ROOT, SUMO_ROUTE_FILE)
        self.v_types = XMLFileEditor.get_attribute(self.sumo_route_file,
                                                   './/vTypeDistribution[@id="typedist1"]',
                                                   'vTypes').split(' ')

    def sensitivity_combinations_simulation(self):
        print("Starting sensitivity analysis...")
        for i in range(ACC_PENETRATION_PERCENTAGE_SPLITS + 1):
            print(f"Processing ACC penetration: {i}/{ACC_PENETRATION_PERCENTAGE_SPLITS}")
            for j in range(SHC_PENETRATION_PERCENTAGE_SPLITS + 1 - i):
                print(f"Processing SHC penetration: {j}/{SHC_PENETRATION_PERCENTAGE_SPLITS}")
                for k in range(IDM_PENETRATION_PERCENTAGE_SPLITS + 1 - i - j):
                    print(f"Processing IDM penetration: {k}/{IDM_PENETRATION_PERCENTAGE_SPLITS}")
                    v_type_distribution = [i * 1.0 / ACC_PENETRATION_PERCENTAGE_SPLITS,
                                           j * 1.0 / SHC_PENETRATION_PERCENTAGE_SPLITS,
                                           k * 1.0 / IDM_PENETRATION_PERCENTAGE_SPLITS]
                    if sum(v_type_distribution) == 1.0:
                        combination_folder_dir = self.create_combination_folder(v_type_distribution)
                        self.edit_route_file(v_type_distribution)
                        self.simulation_handler.montecarlo_simulation(combination_folder_dir)

        print("Sensitivity analysis completed.")

    def edit_route_file(self, v_type_distribution):
        formatted_probabilities = " ".join(["{:.1f}".format(value) for value in v_type_distribution])
        XMLFileEditor.set_attribute(self.sumo_route_file,
                                    './/vTypeDistribution[@id="typedist1"]',
                                    'probabilities', formatted_probabilities)
        print(f"    Edited route file with vType probabilities: {formatted_probabilities}")

    def create_combination_folder(self, v_type_distribution):
        combination_folder_dir = os.path.join(self.simulation_handler.simulations_folder,
                                              "_".join(f"{category}_{value:03d}" for category, value in zip(self.v_types, [int(v * 100) for v in v_type_distribution])))
        os.makedirs(combination_folder_dir)
        print(f"    Created combination folder: '{combination_folder_dir}'")
        return combination_folder_dir
