from abc import ABC, abstractmethod
from visitor import Visitor


class Element(ABC):
    @abstractmethod
    def accept(self, v: Visitor):
        pass
