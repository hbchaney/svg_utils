'''
main function for svg lib 
'''

def main(): 
    #import all lower files 
    import sys
    import os 
    
    #check for input and output file 
    if len(sys.argv) < 3: 
        print("did not input either the file input or output (or both)")
        print("please enter the file input and output after line_trimmer.py")
        return -1
    
    #check if output file already exists 
    if os.path.isfile(sys.argv[2]): 
        print(f"Warning:\nFile {sys.argv[2]} will be overwritten is that okay? (y or [n])")
        in_v = input()
        if in_v != 'y': 
            
        


def processs_data(input_file, output_file): 
    from file.dynamic_path_reader import DynamicPathReader
    from shape.shape import Shape 
    from shape.shape_manager import ShapeManager
    
if __name__ == '__main__': 
    status = main() 
    print(f'exit status {status}')
    
