#edge class that repressent a single segment in a 
import numpy as np

from .coordinate import Coordinate


class Edge : 
    """_summary_
    sasdlkalsd
    """
    
    def __init__(self,_start: Coordinate, _end: Coordinate) -> None:
        self._start = _start
        self._end = _end 
        # self._slope = self._get_slope()
        
    @property
    def start(self) -> Coordinate:
        return self._start
    
    @property
    def end(self) -> Coordinate:
        return self._end
    
    def _get_slope(self) -> float:
        if (self._start.x - self.end.x == 0):
            return np.nan
        vertical_change = self._end.y - self._start.y
        horiz_change = self._end.x - self._end.x
        return vertical_change / horiz_change
        