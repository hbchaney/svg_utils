import logging

from .shape import Shape

class ShapeManager: 
    '''
    stores all shapes and compares them for collisions 
    '''

    def __init__(self): 
        
        self.shape_list : list[Shape] = []
        
    def add_and_compare_shape(self, new_shape : Shape) -> None: 
        
        logging.debug(f'adding shape :\n{new_shape}')
        for i in range(len(self.shape_list)): 
            x = new_shape.compare_lines(self.shape_list[i])
            if x is not None: 
                self.shape_list[i] = x 
                
        for i in range(len(self.shape_list)): 
            x = new_shape.compare_lines(self.shape_list[i])
            if x is not None: 
                self.shape_list[i] = x 
        
        logging.debug(f'cleaned shape : {new_shape}')
        self.shape_list.append(new_shape) 
        
    def get_max_x(self) -> int: 
        
        max_x = 0
        for s in self.shape_list: 
            max_x = max(s.get_max_x(),max_x)
            
        return max_x
    
    def get_max_y(self) -> int: 
        max_y = 0 
        for s in self.shape_list: 
            max_y = max(s.get_max_y(), max_y) 
            
        return max_y

