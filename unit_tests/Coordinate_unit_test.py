import test_setup
test_setup.add_parent() 

from shape.edge import Coordinate
#### Coordinate unit tests 
def run_test(): 
    c1 = Coordinate(1.50003,.749993) 
    c2 = Coordinate(2.49993,3.24999) 

    print(f'print statement check')
    print(c1) 
    print(c2) 

    print('x and y check')
    print(c1.x) 
    print(c1.y) 

    print('x and y distance check')
    print(c1.x_distance(c2))
    print(c1.y_distance(c2))

    print('distance and distance2 check')
    print(c1.distance(c2))
    print(c1.distance2(c2))

    print('add and subtract check') 
    print(c1 + c2) 
    print(c1 - c2) 
    
    
def distance_check(): 
    c1 = Coordinate(1.5,1.5) 
    c2 = Coordinate(1.5,1.5) 
    print(c1.distance(c2))

distance_check()
# run_test()

