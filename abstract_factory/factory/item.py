from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, caption):
        self._caption = caption

    @abstractmethod
    def make_html(self):
        pass