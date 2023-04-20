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
    from file.pathtools import read_paths
    read_paths(input_file,output_file)
    
    
if __name__ == '__main__': 
    status = main() 
    print(f'exit status {status}')
    
