'''
main function for svg lib 
'''

def main(): 
    #import all lower files 
    import sys
    import os 
    
    #check for input and output file 
    if len(sys.argv) < 3: 
        print("ERROR : ")
        print("did not input either the file input or output (or both)")
        print("please enter the file input and output after line_trimmer.py")
        return -1
    
    #check if output file already exists 
    if os.path.isfile(sys.argv[2]): 
        print(f"WARNING :\nFile {sys.argv[2]} will be overwritten is that okay? (y or [n])")
        in_v = input()
        if in_v != 'y':
            print("Exiting") 
            return 0 
        
    #check if input file exists
    if os.path.isfile(sys.argv[1]) == False: 
        print("ERROR : ")
        print("input file does not exist please check the path")
        return -1 
    
    print("Processing Data ...")
    processs_data(sys.argv[1],sys.argv[2])
    return 0 
        


def processs_data(input_file : str, output_file : str) -> None: 
    from file.dynamic_path_reader import DynamicPathReader
    from file.path_writer import PathWriter
    from shape.shape import Shape 
    from shape.shape_manager import ShapeManager
    
    reader = DynamicPathReader(input_file,None)
    writer = PathWriter(output_file,None)
    
    shapes = reader.create_shapes(w_special=True) 
    line_shapes = shapes[0] 
    special_shapes = shapes[1] #data from non line objects 
    
    shape_manager = ShapeManager() 
    for s in line_shapes: 
        shape_manager.add_and_compare_shape(s) 
        
    for s in shape_manager.shape_list: 
        writer.add_path_dvalue(s.get_paths())
        
    #creating special shape master path 
    master_special : list[str] = []
    for special_shape in special_shapes: 
        for str_v in special_shape: 
            master_special.append(str_v)
            
    #cleaning special construction copies
    master_special = list(set(master_special)) 
    master_str = ''
    for cmds in master_special: 
        master_str += cmds 
    
    writer.add_path_dvalue(master_str) 
    writer.create_svg() 
    
    
if __name__ == '__main__': 
    status = main() 
    print(f'exit status {status}')
    
