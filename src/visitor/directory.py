from __future__ import annotations
from entry import Entry
from typing import overload, TYPE_CHECKING
from collections.abc import Iterator

if TYPE_CHECKING:
    from visitor import Visitor


class Directory(Entry):
    _dir = []
    def __init__(self, name):
        self._name = name
        # self._dir = []
    
    def get_name(self) -> str:
        return self._name 
    
    def get_size(self) -> int:
        size = 0
        it = iter(self._dir)
        while (entry := next(it, None)) is not None:
            size += entry.get_size()
        return size
    
    def add(self, entry) -> Entry:
        self._dir.append(entry)
        return self

    def iterator(self) -> Iterator:
        return iter(self._dir)
    
    def accept(self, v: Visitor) -> None:
        v.visit(self)
