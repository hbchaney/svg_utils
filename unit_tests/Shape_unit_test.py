from test_setup import add_parent
add_parent()

from shape import Shape
from shape.bounding_box import BoundingBox
from shape.edge import Line
from shape.edge import Coordinate

def shape_unit(): 
    '''
    unit tests for shape 
    '''

    #Shape 1 
    l1 = Line(Coordinate(-2,2),Coordinate(-2,-2))
    l2 = Line(Coordinate(-2,2),Coordinate(2,2))
    l3 = Line(Coordinate(-2,-2),Coordinate(2,-2))
    l4 = Line(Coordinate(2,2),Coordinate(2,-2))

    s1 = Shape([l1,l2,l3,l4],'rect 1')
    print(s1)

    #Shape 2
    l5 = Line(Coordinate(2,3),Coordinate(2,-3))
    l6 = Line(Coordinate(2,3),Coordinate(4,3))
    l7 = Line(Coordinate(4,3),Coordinate(4,-3))
    l8 = Line(Coordinate(4,-3),Coordinate(2,-3))

    s2 = Shape([l5,l6,l7,l8],'rect 2')
    print(s2)

    s1.compare_lines(s2)

    print(s1)
    return 

shape_unit()