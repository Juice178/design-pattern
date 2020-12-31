from printing import Printing
from banner import Banner

class PrintBanner(Printing):
    def __init__(self, string):
        self.banner = Banner(string)

    def print_weak(self):
        self.banner.show_with_paren()

    def print_strong(self):
        self.banner.show_with_aster()
    
