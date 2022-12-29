from edge import Edge
from edge import Coordinate

class line (Edge) : 
    
    def __init__(self, _start : Coordinate, _end : Coordinate): 
        self._start = _start 
        self._end = _end 
        
    @property 
    def slope(self):
        return self._get_slope() 
    
    def _get_slope(self) -> float:
        if (self._start.x - self.end.x == 0):
            return 'v'
        vertical_change = self._end.y - self._start.y
        horiz_change = self._end.x - self._end.x
        return vertical_change / horiz_change