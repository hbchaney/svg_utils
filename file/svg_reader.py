import os
import sys
from xml.etree import ElementTree as ET

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
__parent_dir__ = os.path.realpath(os.path.join(__location__, ".."))

sys.path.insert(0, __parent_dir__)

from svg_utils import Shape

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
        _root = ET.parse(svg_filepath).getroot()
        for child in _root.findall("xmlns:g/xmlns:path", self._ns):
            print(child.tag, child.attrib)

    def _gen_next_path(root: ):
        pass

    def _parse_path():
        pass
    

if __name__ == '__main__':
    folder = os.path.join(__parent_dir__, "test_files")
    filename = "45_45_60_simplebox_01.svg"

    SvgReader().get_shapes(os.path.join(folder, filename))



