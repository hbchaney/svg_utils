'''
main function for svg lib 
'''
import sys


def trim_svg(argv: list[str]) -> None: 
    #import all lower files 
    import logging
    
    if len(argv) >= 4 and argv[3] == '--debug': 
        logging.basicConfig(level=logging.DEBUG)
    else: 
        logging.basicConfig(level=logging.INFO)
        
    processs_data(argv[1],argv[2])       


def processs_data(input_file : str, output_file : str) -> None: 
    from file.pathtools import read_paths
    read_paths(input_file,output_file)
    
    
if __name__ == '__main__': 
    trim_svg(sys.argv) 
    
