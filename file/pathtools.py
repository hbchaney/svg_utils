import logging
import os
import sys

import svgpathtools

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
__parent_dir__ = os.path.realpath(os.path.join(__location__, ".."))

if __parent_dir__ not in sys.path:
    sys.path.insert(0, __parent_dir__)

from shape import Shape, Coordinate, Line, ShapeManager


def read_paths(input_file, output_file): 
    paths, _, svg_attr = svgpathtools.svg2paths2(input_file)
    manager = ShapeManager()
    
    logging.debug(f'initial paths :\n{paths}')
    other_path = [] 
    
    for shapes in paths: 
        line_list = [] 
        
        for e in shapes: 
            if type(e) == svgpathtools.path.Line: 
                v : complex = e.start
                s_x_val = v.real
                s_y_val = v.imag
                
                e_v = e.end
                e_x_val = e_v.real
                e_y_val = e_v.imag
                line_list.append(
                    Line(
                        Coordinate(s_x_val,s_y_val),
                        Coordinate(e_x_val,e_y_val)
                    )
                )  
                
            else: 
                other_path.append(e)
                
        manager.add_and_compare_shape(Shape(line_list,''))
    
    paths = [] 
    for s in manager.shape_list: 
        l = [] 
        for e in s.edges: 
            l.append(svgpathtools.Line(*e.get_complex()))
            
        paths.append(svgpathtools.Path(*l))
    
    other_path = svgpathtools.Path(*other_path)
    logging.debug(f'nonline ')
    if len(other_path) != 0: 
        paths.append(other_path)
    
    logging.debug(f'final paths :\n{paths}')
    
    svgpathtools.wsvg(paths,svg_attributes=svg_attr, filename = output_file)
    
   
if __name__ == '__main__': 
    in_path = os.path.join(__parent_dir__, 'test_files/Spice_rack_cut_01.svg')
    out_path = os.path.join(__parent_dir__, 'unit_tests/test_outputs/trimmed_spice_rack.svg')
    read_paths(in_path, out_path)
              
