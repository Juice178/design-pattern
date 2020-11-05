from entry import Entry
from multipledispatch import dispatch

class Directory(Entry):
    def __init__(self, name):
        self._name = name
        self._directory = []
    
    def get_name(self):
        return self._name 
    
    def get_size(self):
        size = 0
        for entry in self._directory:
            size += entry.get_size()
        return size
    
    def add(self, entry):
        self._directory.append(entry)
        return self
    
    @dispatch(str)
    def print_list(self, prefix):
        print(f"{prefix} / {self}")
        for entry in self._directory:
            entry.print_list(f"{prefix} / {self._name}")