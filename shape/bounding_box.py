from edge import Edge

class BoundingBox : 
    
    def __init__(self, edges: list[Edge]=None): 
        if edges is not None:
            self.__find_bounding_from_edges(edges) 
        else:  
            self._minx = None
            self._miny = None 
            self._maxx = None
            self._maxy = None
        
    def __find_bounding_from_edges(self,edges) -> None: 
        
        # initializing the edges 
        temp_minx = edges[0].start.x()
        temp_miny = edges[0].start.y()
        temp_maxx = edges[0].start.x()
        temp_maxy = edges[0].start.y() 
        
        
    