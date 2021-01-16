from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context import Context


class State(ABC):
    @abstractmethod
    def do_clock(self, context: 'Context', hour: int) -> None:
        pass

    @abstractmethod
    def do_use(self, context: 'Context') -> None:
        pass 

    @abstractmethod
    def do_alarm(self, context: 'Context') -> None:
        pass 

    @abstractmethod
    def do_phone(self, context: 'Context') -> None:
        pass