
# shape with a combination of edges 
from .edge import Edge
from .bounding_box import BoundingBox

class Shape: 
    """
    I am shape
    """
    
    def __init__(self,
                 _id: str,
                 _edges: list[Edge]=None,
                 ) -> None:  
        if _edges is not None:
            self._edges = _edges 
        else:
            self._edges = list()
        self._id = _id 
        self.__get_bounding_box()
         
    def __get_bounding_box(self) -> None: 
        self.bounding_box = BoundingBox()
        self.bounding_box.set_bounding_box(self._edges)
        
    def reset_bounding_box(self) -> None: 
        #resets the new bounding box
        self.bounding_box = BoundingBox(edges = self._edges) 
        