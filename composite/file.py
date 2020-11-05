from entry import Entry


class File(Entry):
    def __init__(self, name, size):
        self._name = name
        self._size = size

    def get_name(self):
        return self._name
    
    def get_size(self):
        return self._size
    
    def print_list(self, prefix):
        print(f"{prefix}/{self}" )


