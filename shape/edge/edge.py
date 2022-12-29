#edge class that repressent a single segment in a 
import numpy as np

from .coordinate import Coordinate


class Edge : 
    """
    Parent class for all types of path transformations
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
    
    
        
    
    
        