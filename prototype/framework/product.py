from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def use(self, s):
        pass

    @abstractmethod
    def create_clone(self):
        pass

    def __copy__(self):
        return self