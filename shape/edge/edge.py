#edge class that repressent a single segment in a 
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

        
    def get_path(self, move_free : bool = False) -> str: 
        '''
        returns a str repressenting the absolute path of a line
        ''' 
        
        return f'M {self._start._x},{self._start._y} L {self.end._x},{self.end._y}'
    
    
        
    
    
        