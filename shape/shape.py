
# shape with a combination of edges 
from edge import Edge
from bounding_box import BoundingBox

class Shape : 
    
    def __init__(self,
                 _edges : list[Edge],
                 _id : str) -> None:  
        self._edges = _edges 
        self._id = _id 
        self.__get_bounding_box()
         
    def __get_bounding_box(self) -> None: 
        self.bounding_box = BoundingBox()
        self.bounding_box.set_bounding_box(self._edges)
        
    def reset_bounding_box(self) -> None: 
        #resets the new bounding box
        self.bounding_box = BoundingBox(edges = self._edges) 
        