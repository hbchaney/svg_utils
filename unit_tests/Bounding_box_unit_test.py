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
    

def test_line_on_bounding_box(): 
    a_l1 = Line(Coordinate(80,25),
              Coordinate(80,20))
    
    b_l1 = Line(Coordinate(80,25),
              Coordinate(80,17.5))
    
    a_l2 = Line(Coordinate(75,25),
                Coordinate(80,25))
    
    b_l2 = a_l2 
    
    a_l3 = Line(Coordinate(75,25),
                Coordinate(75,20))
    
    b_l3 = a_l3
    
    a = [a_l1,a_l2,a_l3]
    b = [b_l1,b_l2,b_l3]
    
    bbx_a = BoundingBox(a)
    bbx_b = BoundingBox(b)
    print(bbx_a)
    print(bbx_b)
    
    print("intersections : ")
    inter = bbx_a.box_intersection(bbx_b)
    
    print(inter) 
    
    print(inter.edge_intersection(a_l1))
    print(inter.edge_intersection(b_l1))
    


# test_bounding_box() 
# test_2d_bounding()
test_line_on_bounding_box()

