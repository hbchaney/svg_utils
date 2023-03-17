from xml.etree import ElementTree as ET


class PathWriter: 
    
    
    def __init__(self,output_name : str,output_location : str): 
        self.paths = [] 
        self.default_fill = "black"
        self.default_line = "0.265"
        self.svg_output_name = output_name
        self.svg_output_location = output_location
    
    def add_path_dvalue(self, path_d : str): 
        '''
        pulls the path from the shape as a string and creates a sample svg 
        '''
        pass
    
    def create_svg(self): 
        '''
        creates a sample svg with the current pathing information 
        '''
        pass 
    
    