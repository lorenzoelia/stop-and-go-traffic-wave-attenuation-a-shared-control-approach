import os.path

import pandas as pd


class DataSaver:
    @staticmethod
    def export_vehicle_to_csv(vehicle, output_folder):
        data = {
            "time": vehicle.time,
            "position": vehicle.x_position,
            "speed": vehicle.speed,
            "acceleration": vehicle.acceleration,
            "distance_pred": vehicle.distance_pred,
            "timegap_pred": vehicle.timegap_pred,
            "speed_difference_pred": vehicle.speed_difference_pred,
            "type": vehicle.type,
            "arbitration": vehicle.arbitration
        }

        df = pd.DataFrame(data)
        output_file = f"{vehicle.id}.csv"
        df.to_csv(os.path.join(output_folder, output_file), index=False)
