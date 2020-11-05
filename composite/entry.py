from abc import ABC, abstractmethod
from multipledispatch import dispatch

class FileTreatmentException(Exception):
    pass

class Entry(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def add(self, entry):
        raise FileTreatmentException()

    @dispatch(object)
    def print_list(self):
        self.print_list("")

    @abstractmethod
    @dispatch(object, str)
    def print_list(self, prefix):
        pass

    def __str__(self):
        return self.get_name() + "(" + str(self.get_size()) + ")"
