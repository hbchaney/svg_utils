import os
import re
import sys
from xml.etree import ElementTree as ET
from typing import Tuple, Optional

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
__parent_dir__ = os.path.realpath(os.path.join(__location__, ".."))

if __parent_dir__ not in sys.path:
    sys.path.insert(0, __parent_dir__)

from shape import Shape, Coordinate, Edge, Line

class DynamicPathReader: 
    
    # init with file name and location 
    def __init__(self,filename,file_location) -> None:
        self.filename = filename
        self.file_location = file_location 
        
        self.paths = [] 
        _root = ET.parse(file_location + '/' + filename).getroot()
        for child in _root.findall("xmlns:g/xmlns:path", self._ns):
            self.paths.append(child.attrib.get('d'))
    
    



    