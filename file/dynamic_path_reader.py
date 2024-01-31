import os
import re
import sys
from xml.etree import ElementTree as ET
from typing import Tuple, Optional, Union

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
__parent_dir__ = os.path.realpath(os.path.join(__location__, ".."))

if __parent_dir__ not in sys.path:
    sys.path.insert(0, __parent_dir__)

from shape import Shape, Coordinate, Edge, Line
from file.svg_command import svg_command

class DynamicPathReader: 
    
    _ns = {
        "xmlns": "http://www.w3.org/2000/svg"
    }
    
    # init with file name and location 
    def __init__(self,filename : str , file_location : Union[str,None]) -> None:
        self.filename = filename
        self.file_location = file_location 
        
        self.paths = [] 
        if file_location is not None: 
            _root = ET.parse(file_location + '/' + filename).getroot()
        else: 
            _root = ET.parse(filename).getroot()
        for child in _root.findall("xmlns:g/xmlns:path", self._ns):
            self.paths.append(child.attrib.get('d'))
    
    def create_shapes(self,w_special = False) -> list[Shape]: 
        shape_list = [] 
        special = []
        for p in self.paths: 
            data = svg_command.pull_shape_data(p) 
            shape_list.append(Shape(data[0],''))
            special.append(data[1])
        
        if w_special == False: 
            return shape_list
        else: 
            return (shape_list,special)
            
        
            
            
#tests 
if __name__ == '__main__': 
    pass


    