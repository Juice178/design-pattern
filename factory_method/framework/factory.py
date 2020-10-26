from abc import ABC, abstractmethod

class Factory(ABC):
    def create(self, owner):
        p = self._create_product(owner)
        self._register_product(p)
        return p 
    
    @abstractmethod
    def _create_product(self, wner):
        pass

    @abstractmethod
    def _register_product(self, roduct):
        pass