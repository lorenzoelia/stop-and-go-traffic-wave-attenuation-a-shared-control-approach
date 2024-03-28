import xml.etree.ElementTree as ET
import pandas as pd


class XMLToCSVConverter:
    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path

    def parse_xml(self):
        tree = ET.parse(self.xml_file_path)
        root = tree.getroot()
        return root.findall(".//vType")

    def convert_to_csv(self, output_file):
        vtypes = self.parse_xml()

        data = {
            "id": [],
            "color": [],
            "length": [],
            "maxSpeed": [],
            "carFollowModel": [],
            "accel": [],
            "decel": [],
            "tau": [],
            "minGap": [],
            "actionStepLength": [],
            "hControlTimeHeadway": [],
            "cControlTimeHeadway": [],
            "excessTime": [],
            "sigma1": [],
            "sigma2": []
        }

        for vtype in vtypes:
            for attribute in data.keys():
                data[attribute].append(vtype.get(attribute))

        df = pd.DataFrame(data)
        df.set_index("id", inplace=True)
        df.to_csv(output_file)
