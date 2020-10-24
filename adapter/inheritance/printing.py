from abc import ABC, abstractmethod

class Printing(ABC):
    @abstractmethod
    def print_weak(self):
        pass
    @abstractmethod
    def print_strong(self):
        pass