from xml.etree import ElementTree as ET
from typing import Union

class DefaultWriter: 
    
    def __init__(self): 
        self.fill = "none"
        self.stroke = "black"
        self.stroke_width = ".265"
        self.max_x = 100 
        self.max_y = 100 


class PathWriter: 
    
    def __init__(self,
                 output_name : str,
                 output_location : Union[str,None], 
                 defaults : DefaultWriter = DefaultWriter()): 
        
        self.defaults = defaults
        self.svg_output_name = output_name
        self.svg_output_location = output_location
        self.paths = [] 
    
    def add_path_dvalue(self, path_d : str): 
        '''
        pulls the path from the shape as a string and creates a sample svg 
        '''
        self.paths.append(path_d)
    
    def create_svg(self): 
        '''
        creates a sample svg with the current pathing information 
        '''
        svg = ET.Element('svg')
        svg.attrib = {"viewBox" : f'0 0 {self.defaults.max_x} {self.defaults.max_y}'}
        
        for p in self.paths: 
            new_sub = ET.SubElement(svg,'path')
            new_sub.attrib = {
                'fill' : f'{self.defaults.fill}',
                'stroke' : f'{self.defaults.stroke}',
                'stroke-width' : f'{self.defaults.stroke_width}',
                'd': p
            } 
            
        tree = ET.ElementTree(svg)
        ET.indent(tree,'    ')
        if self.svg_output_location is not None: 
            ET.ElementTree.write(tree, 
                                self.svg_output_location + '/' + self.svg_output_name,
                                encoding="utf-8")
        else: 
             ET.ElementTree.write(tree, 
                                self.svg_output_name,
                                encoding="utf-8")
            
    
    def set_max_x(self, max_param : float): 
        '''
        sets the max x for the view box 
        '''
        self.defaults.max_x = max_param
    
    def set_max_y(self, max_param : float): 
        '''
        sets the max y for the view box 
        '''
        self.defaults.max_y = max_param
    
    