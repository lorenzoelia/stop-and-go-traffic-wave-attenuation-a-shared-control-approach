import xml.etree.ElementTree as ET


class XMLFileEditor:
    @staticmethod
    def load_xml(xml_file_path):
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        return tree, root

    @staticmethod
    def set_attribute(xml_file_path, field_path, attribute_name, attribute_value):
        tree, root = XMLFileEditor.load_xml(xml_file_path)
        element = root.find(field_path)
        if element is not None:
            element.set(attribute_name, attribute_value)
            tree.write(xml_file_path)
        else:
            print(f"Error: Element at path '{field_path}' not found.")

    @staticmethod
    def get_attribute(xml_file_path, field_path, attribute_name):
        _, root = XMLFileEditor.load_xml(xml_file_path)
        element = root.find(field_path)
        if element is not None:
            return element.get(attribute_name)
        else:
            print(f"Error: Element at path '{field_path}' not found.")
            return None
