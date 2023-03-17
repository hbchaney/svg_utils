import os
import sys
from typing import Tuple
from xml.etree import ElementTree as ET

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
__parent_dir__ = os.path.realpath(os.path.join(__location__, ".."))

if __parent_dir__ not in sys.path:
    sys.path.insert(0, __parent_dir__)

from path_reader import PathReader
from shape import Shape

class SvgReader:
    """
    The .svg file format is a special case of xml. We also assume that the
    provided .svg files are Inkscape outputs with directions for a laser
    glaive.
    """
    
    _ns = {
        "xmlns": "http://www.w3.org/2000/svg"
    }

    def __init__(self) -> None:
        pass
    

    def get_shapes(self, svg_filepath: str) -> list[Shape]:
        """
        This method parses the provided filepath to a .svg file and returns
        a list of Shape objects.
        """
        shape_arr = list()
        _root = ET.parse(svg_filepath).getroot()
        for obj_id, d in self._gen_next_path_attrib(_root):
            shape_arr.append(self._parse_path(obj_id, d))
        return shape_arr

    def _gen_next_path_attrib(self, root: ET.Element) -> Tuple[str, str]:
        for child in root.findall("xmlns:g/xmlns:path", self._ns):
            yield child.attrib.get('id'), child.attrib.get('d')

    def _parse_path(self, name:str, path: str) -> Shape:
        """
        This method takes a shape's path, as represented by a d tag in the an
        svg file, and creates a PathReader instance to parse it.
        """
        pr = PathReader(name, path)
        pr.parse_path()
        return pr.to_shape()
        





    

if __name__ == '__main__':
    folder = os.path.join(__parent_dir__, "test_files")
    filename = "Spice_rack_cut_01.svg"

    print("" == None)

    shape_arr = SvgReader().get_shapes(os.path.join(folder, filename))
    [print(shapes) for shapes in shape_arr]



   



