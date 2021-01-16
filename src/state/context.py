from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from state import State

class Context(ABC):
    @abstractmethod
    def set_clock(self, hour: int) -> None:
        pass 

    @abstractmethod
    def change_state(self, state: 'State') -> None:
        pass

    @abstractmethod
    def call_secruity_center(self, msg: str) -> None:
        pass 

    @abstractmethod
    def record_log(self, msg: str) -> None:
        pass 

