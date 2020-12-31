class Display:
    def __init__(self, impl):
        self._impl = impl

    def open(self):
        self._impl.raw_open()
    
    def print(self):
        self._impl.raw_print()
    
    def close(self):
        self._impl.raw_close()

    def display(self):
        self.open()
        self.print()
        self.close()