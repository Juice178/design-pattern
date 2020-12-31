class StringBuffer:
    def __init__(self):
         self._strings = []
    
    def append(self, string):
        self._strings.append(string)
    
    def to_string(self):
        return " ".join(self._strings)