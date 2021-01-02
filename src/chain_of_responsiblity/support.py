from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, final
from trouble import Trouble

class Support(ABC):
    def __init__(self, name: str) -> None:
        self._name = name 
        self._next = None # type: Optional[Support]

    def set_next(self, next_support: Support) -> Support:
        self._next = next_support
        return next_support

    @final
    def support(self, trouble: Trouble) -> None:
        if self.resolve(trouble):
            self.done(trouble)
        elif self._next is not None:
            self._next.support(trouble)
        else:
            self.fail(trouble)

    def __str__(self) -> str:
        return f"[ {self._name} ]"

    @abstractmethod
    def resolve(self, trouble: Trouble) -> bool:
        raise NotImplementedError

    def done(self, trouble: Trouble) -> None:
        print(f"{trouble} is resolved by {self}.")

    def fail(self, trouble: Trouble) -> None:
        print(f"{trouble} is cannot be resolved.")
