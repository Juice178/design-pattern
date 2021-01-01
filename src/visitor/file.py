from __future__ import annotations
from entry import Entry
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from visitor import Visitor

class File(Entry):
    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size

    def get_name(self) -> str:
        return self._name
    
    def get_size(self) -> int:
        return self._size
    
    def accept(self, v: Visitor):
        v.visit(self)


