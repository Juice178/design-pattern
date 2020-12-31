from abstract_display import AbstractDisplay
import sys

class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self._string = string
        # Get a byte length
        self._width = len(string.encode("utf-8"))

    def open(self):
        self.print_line()
    
    def print(self):
        print(f"|{self._string}|")

    def close(self):
        self.print_line()

    def print_line(self):
        print('+', end='')
        for i in range(self._width):
            print('-', end='')
        print('+')