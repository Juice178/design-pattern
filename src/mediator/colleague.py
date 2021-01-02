from abc import ABC, abstractmethod
from mediator import Mediator


class Colleague(ABC):
    @abstractmethod
    def set_mediator(self, mediator: Mediator) -> None:
        pass 

    @abstractmethod
    def set_colleague_enabled(self, enabled: bool) -> None:
        pass