from factory.item import Item 

class Tray(Item):
    def __init__(self, caption):
        super().__init__(caption)
        self._tray = []
    
    def add(self, item):
        self._tray.append(item)