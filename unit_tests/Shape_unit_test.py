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
    
    #Shape 3 
    lright = Line(Coordinate(50,10),Coordinate(50,60))
    lleft = Line(Coordinate(10,10),Coordinate(10,60))
    ltop = Line(Coordinate(10,10),Coordinate(50,10))
    lbottom = Line(Coordinate(10,60),Coordinate(50,60))
    s3 = Shape([lright,lleft,ltop,lbottom],"big shape")
    print(s3.get_paths())
    
    print(s3.get_max_x()) 
    print(s3.get_max_y())

    s1.compare_lines(s2)
    s1.compare_lines(s3)

    print(s1)
    return 

shape_unit()