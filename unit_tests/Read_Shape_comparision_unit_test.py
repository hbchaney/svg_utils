from test_setup import add_parent
add_parent()

import os
import sys
import unittest as ut 
from shape import Shape
from shape.edge import Line , Coordinate, Edge
from file.path_writer import PathWriter
from file.path_reader import PathReader
from file.svg_reader import SvgReader

__location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
__parent_dir__ = os.path.realpath(os.path.join(__location__, ".."))

if __parent_dir__ not in sys.path:
    sys.path.insert(0, __parent_dir__)

class ReadandCompareTest(ut.TestCase): 
    
    def setUp(self) -> None:
        folder = os.path.join(__parent_dir__, "test_files")
        filename = "Spice_rack_cut_01.svg"

        self.shapes = SvgReader().get_shapes(os.path.join(folder, filename))
        
    
    def test_read_files(self) -> None: 
        print(self.shapes)
        print(self.shapes[0].edges)
    
    def test_compare_shapes(self) -> None: 
        for i,shapes in enumerate(self.shapes[:len(self.shapes)-1]):
            for shapes in self.shapes[i+1:]:
                self.shapes[i].compare_lines(shapes) 
                
        output_name = "super_test_read_cleaned.svg"
        output_location = r"F:\Projects\Modular Storage Shelf\Python Utilities\svg_utils\test_files"
        self.path_writer = PathWriter(output_name,output_location)
        max_x_list = [] 
        max_y_list = [] 
        for s in self.shapes: 
            self.path_writer.add_path_dvalue(s.get_paths())
            max_x_list.append(s.get_max_x())
            max_y_list.append(s.get_max_y())
        
        self.path_writer.set_max_x(max(max_x_list))
        self.path_writer.set_max_y(max(max_y_list))
        self.path_writer.create_svg()
        
    
    def test_make_svg(self) -> None: 
        output_name = "super_test_read.svg"
        output_location = r"F:\Projects\Modular Storage Shelf\Python Utilities\svg_utils\test_files"
        self.path_writer = PathWriter(output_name,output_location)
        max_x_list = [] 
        max_y_list = [] 
        for s in self.shapes: 
            self.path_writer.add_path_dvalue(s.get_paths())
            max_x_list.append(s.get_max_x())
            max_y_list.append(s.get_max_y())
        
        self.path_writer.set_max_x(max(max_x_list))
        self.path_writer.set_max_y(max(max_y_list))
        self.path_writer.create_svg()
    
    
def tests(): 
    suite = ut.TestSuite() 
    suite.addTest(ReadandCompareTest("setUp"))
    suite.addTest(ReadandCompareTest("test_read_files"))
    suite.addTest(ReadandCompareTest("test_compare_shapes"))
    suite.addTest(ReadandCompareTest("test_make_svg"))
    return suite
    
if __name__ == '__main__': 
    runner = ut.TextTestRunner()
    runner.run(tests())
    




