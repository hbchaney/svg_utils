import os
import re
import sys
from typing import Tuple
from xml.etree import ElementTree as ET

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
__parent_dir__ = os.path.realpath(os.path.join(__location__, ".."))

sys.path.insert(0, __parent_dir__)

from shape import Shape, Coordinate

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
        for d in self._gen_next_path_attrib(_root):
            shape_arr.append(self._parse_path(d))
        return shape_arr

    def _gen_next_path_attrib(self, root: ET.Element) -> None:
        for child in root.findall("xmlns:g/xmlns:path", self._ns):
            yield child.attrib.get('d')

    def _parse_path(self, path: str) -> Shape:
        current_coord = Coordinate(0,0)
        
    def _is_case_one_match(self, path: str) -> Tuple[bool, int]:
        """
        This case returns a boolean indicating whether the next direction
        is a reference (relative or absolute) to a specific coordinate. Also
        returns the integer index for the end of this pattern.
        """
        pattern = r"[mM] ([\-0-9\.]+\,[0-9\.\-]+) "

    def _is_case_two_match(self, path: str) -> Tuple[bool, int]:
        """
        This case returns a boolean indicating where the next direction is a
        horizontal or vertical cut (relative or abosulte). Also returns the 
        integer index of the end of the pattern.
        """
        pattern = r"[vVhH] (([0-9-+\.]+)|([0-9\.]+e\-[0-9]+)) "

    def _is_case_three_match(self, path: str) -> Tuple[bool, int]:
        """
        This case returns true when the next pattern is a line to command
        """
        pattern = r"[lL] ([\-0-9\.]+(|e\-[0-9]))\,([0-9\.\-]+(|e\-[0-9])) "




def parse(filepath: str) -> None:
    pass 


    

if __name__ == '__main__':
    folder = os.path.join(__parent_dir__, "test_files")
    filename = "45_45_60_simplebox_01.svg"

    print("" == None)

    SvgReader().get_shapes(os.path.join(folder, filename))


   



