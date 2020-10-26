from abc import ABC, abstractmethod
from framework import Product

class Factory(ABC):
    def create(self, owner):
        p = self._create_product(owner)
        self._register_product(p)
        assert isinstance(p, Product)
        return p
    
    @abstractmethod
    def _create_product(self, owner):
        pass

    @abstractmethod
    def _register_product(self, product):
        pass