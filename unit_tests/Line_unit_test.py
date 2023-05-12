from test_setup import add_parent
add_parent() 

from shape.edge import Line 
from shape.edge import Coordinate

def Line_test():
    #print test 
    l1 = Line(Coordinate(1.5,1.75),Coordinate(2.5,3.25))
    # v slope 
    l1_5 = Line(Coordinate(1.5,9),Coordinate(1.5,3))
    print(l1)
    print(l1.get_path()) 
    # print(l1_5)
    
    #intercept test 
    l2 = Line(Coordinate(0,-.5),Coordinate(3,4))
    print(l2)
    print(l2.get_path()) 
    
    #check to see if l2 and l1 have some conflicts 
    print(l1.crossing(l2))
    print(l2.cross_type(l2))
    

def Line_Crossing_Types(): 
    
    l1 = Line(Coordinate(80,25),
              Coordinate(80,20))
    
    
    
    l2 = Line(Coordinate(80,25),
              Coordinate(80,17.5))
    
    print(l1.crossing(l2))
    print(l1.cross_type(l2))
    
    
def More_Line_Crossing(): 
    l1 = Line (Coordinate(245.0, 220),
               Coordinate(250, 220))
    
    
    l2 = Line (Coordinate(245.0, 220),
               Coordinate(250, 220))
    
    print("radius")
    
    print(l1.crossing(l2))
    print(l1.cross_type(l2))
    


# Line_test()
More_Line_Crossing()

