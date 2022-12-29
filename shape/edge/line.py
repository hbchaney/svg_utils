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
        
    
    def _get_slope(self) -> float:
        if (self._start.x - self.end.x == 0):
            return 'v'
        vertical_change = self._end.y - self._start.y
        horiz_change = self._end.x - self._end.x
        return vertical_change / horiz_change
    
    def crossing(self, other: "Line") -> bool: 
        
        if self.slope != other.slope : 
            return False
        
        
        
        
        