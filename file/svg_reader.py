import os
import sys
from xml.etree import ElementTree as ET

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))

sys.path.insert(0, __location__)

from shape import Shape

class SvgReader:
    """
    The .svg file format is a special case of xml. We also assume that the
    provided .svg files are Inkscape outputs with directions for a laser
    glaive.
    """
    
    @staticmethod
    def get_shapes(svg_filepath: str) -> list[Shape]:
        """
        This method parses the provided filepath to a .svg file and returns
        a list of Shape objects.
        """
        _root = ET.parse(svg_filepath).getroot()

    @staticmethod
    def _parse_path():
        pass
    

if __name__ == '__main__':
    folder = ""