from shape import Shape

class ShapeManager: 
    '''
    stores all shapes and compares them for collisions 
    '''

    def __init__(self): 
        
        self.shape_list = []
        
    def add_and_compare_shape(self, new_shape : Shape) -> None: 
        
        for i in range(len(self.shape_list)): 
            x = new_shape.compare_lines(self.shape_list[i])
            if x != None: 
                self.shape_list[i] = x 
        
        self.shape_list.append(new_shape) 
        
    



    

