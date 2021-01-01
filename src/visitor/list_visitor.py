from visitor import Visitor
from file import File
from directory import Directory
from typing import overload
from functools import singledispatchmethod


class ListVisitor(Visitor):
    _current_dir = ""

    def __init__(self):
        pass

    @singledispatchmethod
    def visit(self, entry) -> None:
        pass

    @visit.register
    def _(self, file: File) -> None:
        #print("file")
        print(f"{self._current_dir}/{file}")

    @visit.register
    def _(self, directory: Directory) -> None:
        #print("dir")
        print(f"{self._current_dir}/{directory}")
        save_dir = self._current_dir
        # print(f"save_dir: {save_dir}")
        ListVisitor._current_dir = f"{self._current_dir}/{directory.get_name()}"
        # print(f"_current_dir: {self._current_dir}")
        it = directory.iterator()
        while (entry := next(it, None)) is not None:
            entry.accept(self)
        ListVisitor._current_dir = save_dir
    