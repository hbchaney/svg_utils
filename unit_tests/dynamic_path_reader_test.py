from test_setup import add_parent
add_parent()

import unittest as ut 
from shape import Shape
from shape.edge import Line , Coordinate, Edge
from file.path_writer import PathWriter
from file.dynamic_path_reader import DynamicPathReader

class DynamicPathTester(ut.TestCase):
    def setUp(self) -> None:
        pass
    
    def lives_and_dies() -> None: 
        pass


def tests(): 
    suite = ut.TestSuite()
    suite.addTest(DynamicPathReader('lives_and_dies'))

if __name__ == '__main__': 
    runner = ut.TextTestRunner() 
    runner.run(tests())