from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterator
from exception import FileTreatmentException


class Entry(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    def add(self, entry) -> Entry:
        raise FileTreatmentException("It is not possible to add an entry to a file.")

    def iterator(self) -> Iterator:
        pass

    def __str__(self):
        return self.get_name() + " (" + str(self.get_size()) + ")"
