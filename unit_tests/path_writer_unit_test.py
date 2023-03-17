from test_setup import add_parent
add_parent()

import unittest as ut 
from shape import Shape
from shape.edge import Line , Coordinate, Edge
from file.path_writer import PathWriter

class PathWriterTests(ut.TestCase): 
    
    def setUp(self): 
        output_name = "test_svg"
        output_location = r"F:\Projects\Modular Storage Shelf\Python Utilities\svg_utils\test_files"
        self.path_writer = PathWriter(output_name,output_location)
        print()
        return 
    
    def test_add_path(self): 
        
        lright = Line(Coordinate(50,10),Coordinate(50,60))
        lleft = Line(Coordinate(10,10),Coordinate(10,60))
        ltop = Line(Coordinate(10,10),Coordinate(50,10))
        lbottom = Line(Coordinate(10,60),Coordinate(50,60))
        s3 = Shape([lright,lleft,ltop,lbottom],"big shape")
        
        lright = Line(Coordinate(40,20),Coordinate(40,30))
        lleft = Line(Coordinate(20,20),Coordinate(20,30))
        ltop = Line(Coordinate(20,20),Coordinate(40,20))
        lbottom = Line(Coordinate(20,30),Coordinate(40,30))
        s4 = Shape([lright,lleft,ltop,lbottom],"small shape")
        
        self.path_writer.add_path_dvalue(s3.get_paths())
        self.path_writer.add_path_dvalue(s4.get_paths())
        
        print(self.path_writer.paths)
        
    def test_create_svg(self): 
        self.test_add_path() 
        self.path_writer.create_svg()


def tests(): 
    suite = ut.TestSuite() 
    suite.addTest(PathWriterTests('setUp'))
    suite.addTest(PathWriterTests('test_add_path'))
    suite.addTest(PathWriterTests('test_create_svg'))
    return suite 

if __name__ == '__main__': 
    runner = ut.TextTestRunner()
    runner.run(tests())