from display_impl import DisplayImpl

class StringDisplayImpl(DisplayImpl):
    def __init__(self, string):
        self._string = string
        self._width = len(string.encode("utf-8"))
    
    def raw_open(self):
        self.print_line()

    def raw_print(self):
        print(f"|{self._string}|")
    
    def raw_close(self):
        self.print_line()
    
    def print_line(self):
        print("+", end="")
        for _ in range(self._width):
            print("-", end="")
        print("+")