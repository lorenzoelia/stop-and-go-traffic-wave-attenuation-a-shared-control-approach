import xml.etree.ElementTree as ET

from numpy import random

from stop_and_go_traffic_wave_attenuation_a_shared_control_approach.config import ROUTE_LENGTH


class DemandGenerator:
    def __init__(self, xml_file):
        self.xml_file = xml_file

    def set_density(self, num_routes, num_vehicles_per_route, starting_speed):
        tree = ET.parse(self.xml_file)
        root = tree.getroot()
        self.remove_existing_vehicles(root)
        total_vehicles = 0
        for route_id in range(num_routes):  # Assuming 4 routes as per your XML structure
            route = root.find(f"./route[@id='r_{route_id}']")
            if route is not None:
                self.remove_existing_vehicles(route)
                total_vehicles += num_vehicles_per_route
                self.add_vehicles_to_route(root, route, route_id, num_vehicles_per_route, total_vehicles, starting_speed)

        tree.write(self.xml_file, encoding="utf-8", xml_declaration=True)

    def remove_existing_vehicles(self, root):
        for vehicle in root.findall(".//vehicle"):
            root.remove(vehicle)

    def add_vehicles_to_route(self, root, route, route_id, num_vehicles_per_route, total_vehicles, starting_speed):
        if route is not None:
            route_length = ROUTE_LENGTH
            equidistant_position = route_length / num_vehicles_per_route

            for i in range(total_vehicles - num_vehicles_per_route, total_vehicles):
                vehicle_id = f"veh{i:02d}"
                depart_pos = (i - (total_vehicles - num_vehicles_per_route)) * equidistant_position
                vehicle = ET.SubElement(root, "vehicle", id=vehicle_id, type="typedist1",
                                        route=f"r_{route_id}", depart="0", departPos=f"{depart_pos:.2f}",
                                        departSpeed=f"{random.normal(5.0, 1.0)}", speedFactor="1.0", insertionChecks="none")
                vehicle.tail = '\n\t'
