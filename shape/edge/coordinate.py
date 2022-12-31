import math

#class for handling the coordinate 

class Coordinate: 
    
    def __init__(self,_x: float,_y: float) -> None: 
        self._x = self._rounded(_x) 
        self._y = self._rounded(_y) 
        
    @property
    def x(self) -> float: 
        return self._x 
    
    @property
    def y(self) -> float: 
        return self._y
    
    def handle_float_error(self) -> None: 
        self._x = round(self._x, 3) 
        self._y = round(self._y, 3) 
        
    def _rounded(self, f: float) -> float:
        return round(f, 3)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return f"({self._x}, {self._y})"
    
    def x_distance(self, other: "Coordinate") -> float: 
        '''
        distance between two x components
        '''
        return abs(self.x - other.x) 
    
    def y_distance(self, other: "Coordinate") -> float: 
        '''
        distance between two y components
        '''
        return abs(self.y - other.y)
    
    def distance(self, other: "Coordinate") -> float: 
        '''
        distance between two Coordinates (caution uses sqrt)
        '''
        return math.sqrt((self.x_distance(other))**2 + (self.y_distance(other))**2)
    
    def distance2(self, other: "Coordinate") -> float: 
        '''
        returns the distance squared between two points 
        '''
        return (self.x_distance(other))**2 + (self.y_distance(other))**2
    
    def __add__(self, other: "Coordinate") -> "Coordinate": 
        return Coordinate(self.x + other.x, self.y + other.y) 
    
    def __sub__(self,other: "Coordinate") -> "Coordinate": 
        return Coordinate(self.x - other.x,self.y - other.y)
    
    