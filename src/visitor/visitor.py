from __future__ import annotations
from abc import ABC, abstractmethod
from file import File
from directory import Directory
# from file import File
from typing import overload, TYPE_CHECKING
from functools import singledispatchmethod

if TYPE_CHECKING:
    from visitor import File, Directory


class Visitor(ABC):
    def __init__(self):
        pass

    @singledispatchmethod
    @abstractmethod
    def visit(self, entry) -> None:
        raise NotImplementedError

    # # @overload
    # @visit.register
    # @abstractmethod
    # def _(self, entry: File) -> None:
    #     pass

    # # @overload
    # @visit.register
    # @abstractmethod
    # def _(self, entry: Directory) -> None:
    #     pass