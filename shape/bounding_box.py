from .edge import Edge
from .edge import Line
from .edge import Coordinate

class BoundingBox : 
    
    def __init__(self, edges: list[Edge]=None, data_in : list[Coordinate,float] = None) -> None: 
        if edges is not None:
            self.__find_bounding_from_edges(edges) 
            return
        elif data_in is not None: 
            self._midpoint = data_in[0] 
            self._rx = data_in[1] 
            self._ry = data_in[2] 
            return 
        else:  
            self._midpoint = None
            self._rx = None
            self._ry = None 
        
        
    def __find_bounding_from_edges(self,edges : list[Edge]) -> None: 
        
        # initializing the edges 
        temp_minx = edges[0].start.x
        temp_miny = edges[0].start.y
        temp_maxx = edges[0].start.x
        temp_maxy = edges[0].start.y
        
        #going through each edge 
        for e in edges: 
            #max x 
            if e.start.x >= temp_maxx: 
                temp_maxx = e.start.x
            if e.end.x >= temp_maxx: 
                temp_maxx = e.end.x
                
            #min x 
            if e.start.x <= temp_minx: 
                temp_minx = e.start.x
            if e.end.x <= temp_minx: 
                temp_minx = e.end.x
            
            #max y 
            if e.start.y >= temp_maxy: 
                temp_maxy= e.start.y 
            if e.end.y >= temp_maxy: 
                temp_maxy = e.end.y 
                
            #min y 
            if e.start.y <= temp_miny: 
                temp_miny = e.start.y 
            if e.end.y <= temp_miny: 
                temp_miny = e.end.y 
                
        #### Calculating the mid point and rx + ry 
        mid_x = (temp_maxx-temp_minx)/2 + temp_minx
        mid_y = (temp_maxy-temp_miny)/2 + temp_miny
        self._midpoint = Coordinate(mid_x,mid_y)
        
        rx = (temp_maxx - temp_minx) / 2
        ry = (temp_maxy - temp_miny) / 2
        
        self._rx = rx
        self._ry = ry 
        
        
    
    def set_bounding_box(self,edges : list[Edge]) -> None: 
        self.__find_bounding_from_edges(edges) 
        
        
    def get_data(self): 
        return [self._midpoint,self._rx,self._ry].copy() 
    
    #different for different self/other fixed
    def box_intersection(self, other: "BoundingBox") -> "BoundingBox": 
        temp = other.get_data()
        
        other_mid = temp[0] 
        other_rx = temp[1] 
        other_ry = temp[2] 
        
        #check if boxes are on top of each other 
        if other_mid.x - self._midpoint.x == 0 and other_mid.y - self._midpoint.y == 0: 
            tx = min(self._rx,other_rx)
            ty = min(self._ry,other_ry)
            return BoundingBox(data_in=[self._midpoint,tx,ty])
    
        
        #compare if the x and y are in range 
        if abs(self._midpoint.x - other_mid.x) <= self._rx + other_rx and abs(self._midpoint.y - other_mid.y) <= self._ry + other_ry:
            new_rx = (-abs(self._midpoint.x - other_mid.x) + (self._rx + other_rx)) / 2
            new_ry = (-abs(self._midpoint.y - other_mid.y) + (self._ry + other_ry)) / 2 
            
            if (other_mid.x-self._midpoint.x) != 0: 
                dir_x = ((other_mid.x-self._midpoint.x)/abs(other_mid.x-self._midpoint.x))
            else: 
                dir_x = 0 
            if (other_mid.y-self._midpoint.y) != 0: 
                dir_y = ((other_mid.y-self._midpoint.y)/abs(other_mid.y-self._midpoint.y))
            else: 
                dir_y = 0
            
            new_mid_x = self._midpoint.x +  dir_x*self._rx + -1*dir_x*new_rx
            new_mid_y = self._midpoint.y + dir_y*self._ry + -1*dir_y*new_ry 
            
            return BoundingBox(data_in = [Coordinate(new_mid_x,new_mid_y),new_rx,new_ry])

        else: 
            return None
    
    #not capturing correctly   
    def edge_intersection(self, edge : Edge) -> bool:
        
        line = Line(edge.start,edge.end)
        x_tolerance = abs(edge.start.x - edge.end.x)/2
        y_tolerance = abs(edge.start.y - edge.end.y)/2
        
        x_distance = abs(self._midpoint.x - line.midpoint.x) 
        y_distance = abs(self._midpoint.y - line.midpoint.y)
        
        if (x_distance > self._rx + x_tolerance): 
            return False 
        if (y_distance > self._ry + y_tolerance): 
            return False 

        #2d edge case 

        return True 
        
        # ^ needs some testing 
    
    def __str__(self): 
        return f'middle : {self._midpoint}\nrx : {self._rx}\nry : {self._ry}'
        
        
        
        
        
    
        
        
    