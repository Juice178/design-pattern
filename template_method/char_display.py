from abstract_display import AbstractDisplay

class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self._ch = ch   
    
    def open(self):
        print("<<", end="")
    
    def print(self):
        print(self._ch, end="")

    def close(self):
        print(">>")