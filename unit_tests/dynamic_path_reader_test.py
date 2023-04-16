from test_setup import add_parent
add_parent()

from file import svg_command
import os
import unittest as ut 
from shape import Shape
from shape.shape_manager import ShapeManager
from shape.edge import Line , Coordinate, Edge
from file.path_writer import PathWriter
from file.dynamic_path_reader import DynamicPathReader

class DynamicPathTester(ut.TestCase):
    
    def setUp(self) -> None:
        test_files = os.listdir('./test_files/basic_examples')
        check_output = os.path.isdir('./unit_tests/test_outputs')
        self.assertTrue(check_output)
        self.assertGreater(len(test_files),0)
        
        self.reader = DynamicPathReader(test_files[0],'./test_files/basic_examples')
        
        #output reader 
        self.writer = PathWriter('dynamic_tester1.svg','./unit_tests/test_outputs')
        self.writer2 = PathWriter('compare_shapes2.svg','./unit_tests/test_outputs')
    
    def lives_and_dies(self) -> None: 
        test_files = os.listdir('./test_files/basic_examples')
        output = os.path.isdir('./unit_tests/test_outputs')
        
        DynamicPathReader(test_files[0],'./test_files/basic_examples')
        
    def read_and_write_shape(self) -> None: 
        shapes = self.reader.create_shapes()
        print(shapes)
        for s in shapes: 
            self.writer.add_path_dvalue(s.get_paths())
        self.writer.create_svg()
        
    def compare_shapes(self) -> None: 
        shapes = self.reader.create_shapes()
        shape_manager = ShapeManager()
        for s in shapes: 
            shape_manager.add_and_compare_shape(s)  
        for s in shape_manager.shape_list: 
            self.writer2.add_path_dvalue(s.get_paths())
        self.writer2.create_svg()
        
    

    
    


def tests(): 
    suite = ut.TestSuite()
    suite.addTest(DynamicPathTester('setUp'))
    suite.addTest(DynamicPathTester('lives_and_dies'))
    suite.addTest(DynamicPathTester("read_and_write_shape"))
    suite.addTest(DynamicPathTester('compare_shapes'))
    return suite

if __name__ == '__main__': 
    runner = ut.TextTestRunner() 
    runner.run(tests())
    