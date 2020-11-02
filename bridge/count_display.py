from display import Display

class CountDisplay(Display):
    def __init__(self, impl):
        super().__init__(impl)
    
    def multi_display(self, times):
        self.open()
        for _ in range(times):
            self.print()
        self.close()