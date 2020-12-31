from builder import Builder
from string_buffer import StringBuffer

class TextBuilder(Builder):
    def __init__(self):
        self._buffer = StringBuffer()
    def make_title(self, title):
        self._buffer.append("==============================\n")
        self._buffer.append(f"[     {title}      ]\n")
        self._buffer.append("\n")
    
    def make_string(self, string):
        self._buffer.append(f"■ {string} \n")
        self._buffer.append(f"\n")

    def make_items(self, items):
        for i in range(len(items)):
            self._buffer.append(f" ・{items[i]}\n" )
        self._buffer.append("\n")
    
    def close(self):
        self._buffer.append("====================\n")

    def get_result(self):
        return self._buffer.to_string()