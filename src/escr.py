# custom file saving
import os
import re

class ESCR:
    def __init__(self):
        pass
        # self.filepath = filepath

    def read(self, filepath):
        # read the file
        # note : beutify it
        with open(filepath, "r") as file:
            print(file.read())

    def write(self, filepath):
        # write to file
        # note : beutify it
        pass