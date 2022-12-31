from typing import Union

from edge import Edge
from edge import Coordinate


class Line (Edge) : 
    
    def __init__(self, _start : Coordinate, _end : Coordinate): 
        super().__init__(_start,_end)
        
    @property 
    def slope(self) -> float:
        return self._get_slope() 
    
    @property 
    def midpoint(self) -> Coordinate:
        mid_x = (self._start.x + self._end.x) / 2
        mid_y = (self._start.y + self._end.y) / 2
        return Coordinate(mid_x,mid_y)
    
    @property
    def intercept(self) -> float: 
        '''
        returns the y intercept unless the slope is 'v' than returns the x intercept
        '''
        slope = self.slope 
        if slope == 'v': 
            return self.midpoint.x
        return self.midpoint.y - self.midpoint.x * self.slope
    
    @property 
    def radius(self) -> float: 
        return self.start.distance(self.end) / 2
        
    
    def _get_slope(self) -> float:
        if (self._start.x - self.end.x == 0):
            return 'v'
        vertical_change = self._end.y - self._start.y
        horiz_change = self._end.x - self._end.x
        return vertical_change / horiz_change
    
    def crossing(self, other: "Line") -> bool: 
        
        #determine if lines have the same slope 
        if self.slope != other.slope : 
            return False
        if self.intercept != self.intercept: 
            return False 
        
        max_distance = self.radius + other.radius
        mid_distance = self.midpoint.distance(other.midpoint)
        
        if mid_distance < max_distance: 
            return True
        else: 
            return False
        
    def cross_type(self,other: "Line") -> Union[int,list("Line")]: 
        '''
        determines the type of crossing that has occured and returns the condition 
        1 : either can be deleted 
        2 : self should be deleted 
        3 : other should be deleted 
        4 : special case returns new line for self and new line for other 
        '''
        
        if self.radis * 2 == other.radius * 2: 
            
        #determine if the lines lie on the same line 
        
        
        
        
        
        