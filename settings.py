
# settings.py

import xml.etree.ElementTree as ET

class UserSettings:
    def __init__(self):
        self.selected_frequency = ""
        self.selected_marker_size = ""
        self.selected_unit = ""
        self.selected_marker = ""
        self.selected_color = ""
        self.selected_font = ""
        self.selected_horiz_grid = ""
        self.selected_vertic_grid = ""
        self.selected_graph_width = 0
        self.selected_graph_height = 0
        self.selected_detrending = ""

    def set_frequency(self, value):
        self.selected_frequency = value

    def set_detrending(self, value):
        self.selected_detrending = value

    def set_marker_size(self, value):
        self.selected_marker_size = value

    def set_vertical_grid(self, value):
        self.selected_vertic_grid = value


    def set_unit(self, value):
        self.selected_unit = value
    
    def set_marker(self, value):
        self.selected_marker = value

    def set_color(self, value):
        self.selected_color = value

    def set_font(self, value):
        self.selected_font = value

    def set_horizontal_grid(self, value):
        self.selected_horiz_grid = value

    def set_graph_width(self, value):
        self.selected_graph_width = value

    def set_graph_height(self, value):
        self.selected_graph_height = value

    


    def save_to_xml(self, filename):
        root = ET.Element("UserSettings")
        
        ET.SubElement(root, "Frequency").text = self.selected_frequency
        ET.SubElement(root, "Detrending").text = self.selected_detrending
        ET.SubElement(root, "MarkerSize").text = self.selected_marker_size
        ET.SubElement(root, "Unit").text = self.selected_unit
        ET.SubElement(root, "Marker").text = self.selected_marker
        ET.SubElement(root, "Color").text = self.selected_color
        ET.SubElement(root, "Font").text = self.selected_font
        ET.SubElement(root, "HorizontalGrid").text = self.selected_horiz_grid
        ET.SubElement(root, "VerticalGrid").text = self.selected_vertic_grid
        ET.SubElement(root, "GraphWidth").text = str(self.selected_graph_width)
        ET.SubElement(root, "GraphHeight").text = str(self.selected_graph_height)

        tree = ET.ElementTree(root)
        with open(filename, "wb") as xml_file:
            tree.write(xml_file)
