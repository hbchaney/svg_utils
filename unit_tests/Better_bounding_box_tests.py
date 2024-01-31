from test_setup import add_parent
add_parent()

from file import svg_command
import os
import unittest as ut 
from shape import Shape
from shape.bounding_box import BoundingBox
from shape.shape_manager import ShapeManager
from shape.edge import Line , Coordinate, Edge
from file.path_writer import PathWriter
from file.dynamic_path_reader import DynamicPathReader

class BoundingboxTester(ut.TestCase):
    
    def setUp(self) -> None:
        test_files = os.listdir('./test_files/basic_examples')
        check_output = os.path.isdir('./unit_tests/test_outputs')
        self.assertTrue(check_output)
        self.assertGreater(len(test_files),0)
        
        self.reader = DynamicPathReader(test_files[0],'./test_files/basic_examples')
        self.shapes : list[Shape] = self.reader.create_shapes() 
        
        self.bounding_boxes : list[BoundingBox] = [] 
        for s in self.shapes: 
            self.bounding_boxes.append(s.bounding_box)
            
    def print_bounding_boxes(self) -> None: 
        for i in self.bounding_boxes: 
            print(i) 
            
    def check_intersections(self): 
        
        intersect_boxes = [] 
        
        for i in range(len(self.bounding_boxes) - 1): 
            
            for v in self.bounding_boxes[i+1:]: 
                
                out = self.bounding_boxes[i].box_intersection(v)
                if out != None: 
                    intersect_boxes.append(out) 
                    
        for intersect in intersect_boxes:
            print(intersect)
            for shape in self.shapes: 
                print(shape)
                for edge in shape.edges: 
                    print(edge)
                    print(intersect.edge_intersection(edge))
                
            
            
            
            
    
    
def tests(): 
    suite = ut.TestSuite() 
    suite.addTest(BoundingboxTester('setUp'))
    # suite.addTest(BoundingboxTester('print_bounding_boxes'))
    suite.addTest(BoundingboxTester('check_intersections'))
    return suite 

if __name__ == '__main__': 
    runner = ut.TextTestRunner() 
    runner.run(tests())