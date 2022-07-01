# standard imports
import pathlib
# external imports

# project imports
from pycli.utilities import abs_path

class PyExtractor(object):

    def __init__(self):
        self.name = "A python extractor object"
    
    def read_requirements(self, fpath: str):
        path_to_read = abs_path(fpath=fpath)
        with open(path_to_read, "r") as infile:
            text = infile.read()
        print(text)