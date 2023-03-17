
# shape with a combination of edges 
from .edge import Edge
from .edge import Line
from .bounding_box import BoundingBox

class Shape: 
    """
    shape class that contains edge data 
    """
    
    def __init__(self,
                 _edges : list[Edge],
                 _id : str) -> None:  
        self.edges = _edges 
        self._id = _id 
        self.__get_bounding_box()
         
    def __get_bounding_box(self) -> None: 
        self.bounding_box = BoundingBox()
        self.bounding_box.set_bounding_box(self.edges)
        
    def reset_bounding_box(self) -> None: 
        #resets the new bounding box
        self.bounding_box = BoundingBox(edges = self.edges) 

    def compare_lines(self, other: "Shape") -> None: 
        '''
        compares the lines of self and other and determines what to do with the edges 
        '''

        #find the the overlap box 
        collision_box = self.bounding_box.box_intersection(other.bounding_box)
        if collision_box is None: 
            return 
        

        #list of indicies to compare 
        self_to_compare = [] 
        other_to_compare = [] 

        #list of lines to be deleted 
        self_to_delete = [] 
        other_to_delete = [] 

        for i,edges in enumerate(self.edges): 
            if type(edges) == Line and collision_box.edge_intersection(edges):
                self_to_compare.append(i) 

        for i,edges in enumerate(other.edges): 
            if type(edges) == Line and collision_box.edge_intersection(edges): 
                other_to_compare.append(i) 

        #compare each line the in collision box to see if there are any collisions 
        for i in self_to_compare: 

            for j in other_to_compare: 
                
                if self.edges[i].crossing(other.edges[j]): 
                    crs_type = self.edges[i].cross_type(other.edges[j])

                    if type(crs_type) == Line: 
                        self.edges[i] = crs_type
                        other_to_delete.append(j) 
                        break

                    if crs_type == 1 or crs_type == 2: 
                        self_to_delete.append(i)
                        break
                    elif crs_type == 3: 
                        other_to_delete.append(j) 
                        break
                        

        #sort the delete list backwards 
        self_to_delete = sorted(self_to_delete,reverse=True)
        other_to_delete = sorted(other_to_delete,reverse=True) 

        for values in self_to_delete: 
            del self.edges[values] 
        for values in other_to_delete: 
            del other.edges[values]

        return 

    def __str__(self) -> None: 
        '''
        returns some descriptors: 
            edges 
            the bounding box 
        '''
        bb = self.bounding_box
        ed = self.edges 
        return (f'shape id : {self._id}\nboudingbox: \n{bb}\nno egdes : {len(ed)}\nedges : \n{ed}')
    
    def get_paths(self) -> str: 
        '''
        returns the full path of all the edges in the shape 
        ''' 
        long_str = ''
        for e in self.edges: 
            long_str += e.get_path() + ' '
                
        return long_str
    
    def get_max_x(self) -> float: 
        
        def x_key(edge_value : Edge) -> float: 
            return max([edge_value.start.x,edge_value.end.x])
        
        max_x_edge = max(self.edges,key=x_key)
        return max(max_x_edge.start.x,max_x_edge.end.x)
    
    def get_max_y(self) -> float: 
        
        def y_key(edge_value : Edge) -> float: 
            return max([edge_value.start.y,edge_value.end.y])
        
        max_y_edge = max(self.edges,key=y_key)
        return max(max_y_edge.start.y,max_y_edge.end.y) 
        


        