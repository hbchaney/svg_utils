
# shape with a combination of edges 
from edge import Edge
from bounding_box import BoundingBox
class Shape : 
    
    def __init__(self,
                 _edges : Edge,
                 _id : str) -> None:  
        self._edges = _edges 
        self._id = _id 
        
    @property
    def set_bounding_box(self) -> BoundingBox: 
        return 