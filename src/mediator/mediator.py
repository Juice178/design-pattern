from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def craete_colleagues(self) -> None:
        pass

    @abstractmethod
    def colleague_changed(self) -> None:
        pass