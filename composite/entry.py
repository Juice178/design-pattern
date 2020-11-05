from abc import ABC, abstractmethod
from pythonlangutil.overload import Overload, signature

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
        raise FileTreatmentException("It is not possible to add an entry to a file.")

    @Overload
    @signature("str")
    def print_list(self, prefix):
        pass

    @print_list.overload
    @signature()
    def print_list(self):
        self.print_list("")


    def __str__(self):
        return self.get_name() + " (" + str(self.get_size()) + ")"
