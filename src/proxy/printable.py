from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def set_printer_name(self, name: str) -> None:
        pass
    @abstractmethod
    def get_printer_name(self) -> str:
        pass
    @abstractmethod
    def print(self, string: str) -> None:
        pass