from test_setup import add_parent
add_parent() 

from shape.bounding_box import BoundingBox
from shape.edge import Line
from shape.edge import Coordinate

def test_bounding_box() -> None: 
    '''
    tests bounding box functions 
    '''


    #### initialization 

    l1 = Line(Coordinate(-2,2),Coordinate(2,2))
    l2 = Line(Coordinate(-2,-2),Coordinate(2,-2))
    l3 = Line(Coordinate(-1,3),Coordinate(3,3))
    l4 = Line(Coordinate(-1,1),Coordinate(3,-1))


    bb1 = BoundingBox()
    bb2 = BoundingBox()

    
    bb1.set_bounding_box([l1,l2])
    bb2.set_bounding_box([l3,l4]) 
    print(bb1)
    print(bb2)

    #### bounding box to bounding box intersection
    #intersection exists 
    print(bb1.box_intersection(bb2))
    #intersection does not exist

    i1 = Line(Coordinate(1,4),Coordinate(1,2)) #special no case
    i2 = Line(Coordinate(2,1),Coordinate(4,1)) #other special no case
    i3 = Line(Coordinate(-2,1),Coordinate(-2,-1)) # this should intersect 
    i4 = Line(Coordinate(1,-1),Coordinate(-1,-1)) # also should intersect
    i5 = Line(Coordinate(-1,0),Coordinate(-1,1)) # also should intersect 
    print(bb1.edge_intersection(i1))
    print(bb1.edge_intersection(i2))
    print(bb1.edge_intersection(i3)) 
    print(bb1.edge_intersection(i4))
    print(bb1.edge_intersection(i5))

    #### check if a line is intersecting with the bouding box 
    print(bb1.edge_intersection(l4))


def test_2d_bounding (): 
    '''
    tests if a 2d bounding box is created when 2 
    '''
    
    l1 = Line(Coordinate(0,2),Coordinate(2,2))
    l2 = Line(Coordinate(0,0),Coordinate(0,2))
    l3 = Line(Coordinate(2,2),Coordinate(2,-2))
    
    l_test = Line(Coordinate(2,1),Coordinate(2,0))
    # print(l_test) 


    bb1 = BoundingBox()
    bb2 = BoundingBox()

    
    bb1.set_bounding_box([l1,l2])
    bb2.set_bounding_box([l3]) 
    
    bb3 = bb1.box_intersection(bb2)
    print(bb3)
    
    print(bb3.edge_intersection(l_test))
    
    
    # print(bb1)
    # print(bb2)
    




# test_bounding_box() 
test_2d_bounding()