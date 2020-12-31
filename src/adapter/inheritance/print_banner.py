from banner import Banner
from printing import Printing

class PrintBanner(Printing, Banner):
    def __init__(self, string):
        super().__init__(string)
    
    def print_weak(self):
        super().show_with_paren()

    def print_strong(self):
        super().show_with_aster()

    