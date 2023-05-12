from .edge import Edge
from .coordinate import Coordinate


class Line(Edge) : 
    
    def __init__(self, _start : Coordinate, _end : Coordinate): 
        super().__init__(_start,_end)
        self._radius = None 
        self._slope = None 
        self._midpoint = None 
        self._intercept = None
        
    def __str__(self): 
        return f'slope : {self.slope}\nmidpoint : {self.midpoint}'
    
    def __repr__(self) -> str:
        return f'(Start {self._start} , End {self._end})'
        
    @property 
    def slope(self) -> float:
        if self._slope is not None:
            return self._slope 
        else: 
            self._slope = self._get_slope() 
            return self._slope
    
    @property 
    def midpoint(self) -> Coordinate:
        if self._midpoint is None: 
            mid_x = (self._start.x + self._end.x) / 2
            mid_y = (self._start.y + self._end.y) / 2
            self._midpoint = Coordinate(mid_x,mid_y)
            return self._midpoint
        else: 
            return self._midpoint
    
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
        if self._radius is None:
            self._radius = self.start.distance(self.end) / 2
            return self._radius
        else: 
            return self._radius
    
    def _get_slope(self) -> float:
        if (self._start.x == self._end.x):
            return 'v'
        vertical_change = self._end.y - self._start.y
        horiz_change = self._end.x - self._start.x
        return round(vertical_change / horiz_change, 3)
    
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
        
    def cross_type(self,other: "Line"): 
        '''
        determines the type of crossing that has occured and returns the condition 
        1 : either can be deleted 
        2 : self should be deleted 
        3 : other should be deleted 
        4 : returns a new line to replace self with delete the other line
        '''
        
        print("comparing : ")
        print(self)
        print(other)
        
        if self._radius == other.radius and self.midpoint == other.midpoint: 
            return 1
        
        m_d = self.midpoint.distance(other.midpoint)
        if m_d + other.radius < self._radius: 
            return 3
        elif m_d + self.radius < other.radius: 
            return 2
        else: 
            #check the slope 
            checks = [self._start,self._end,other.start,other.end]
            if self._slope != 0: 
                #looks for the y coordinates on the extremes
                top = max(checks,key = lambda point : point.y)
                bottom = min(checks,key = lambda point : point.y) 
                return Line(bottom,top) 

            else:
                #looks for the x coordinates on the extremes 
                top = max(checks,key = lambda point : point.x) 
                bottom = min(checks, key = lambda point : point.x) 
                return Line(top,bottom) 
            
        

    def get_path(self) -> str: 
        '''
        returns a str repressenting the absolute path of a line
        ''' 
        
        return f'M {self._start._x},{self._start._y} L {self.end._x},{self.end._y}'
    

        
        
        
        
        
        
        