from framework import Product
from copy import copy


class MessageBox(Product):
    def __init__(self, decochar):
        self._decochar = decochar
    
    def use(self, s):
        length = len(s.encode('utf-8'))
        for _ in range(0, length+4):
            print(self._decochar, end="")
        print("")
        print(f"{self._decochar} {s} {self._decochar}")
        for _ in range(0, length+4):
            print(self._decochar, end="")
        print("")
    
    def create_clone(self):
        p = copy(self)
        return p


        