import sys, os 
def add_parent(): 
    __location__ = os.path.join(os.getcwd(), os.path.dirname(__file__))
    __parent_dir__ = os.path.realpath(os.path.join(__location__, ".."))

    sys.path.insert(0, __parent_dir__)