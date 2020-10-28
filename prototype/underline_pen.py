from framework import Product
from copy import copy


class UnderlinePen(Product):
    def __init__(self, ulchar):
        self._ulchar = ulchar
    
    def use(self, s):
        length = len(s.encode('utf-8'))
        print(f"{ s }")
        # print(" ")
        for _ in range(0, length+4):
            print(self._ulchar, end="")
        print("")
    
    def create_clone(self):
        p = copy(self)
        return p