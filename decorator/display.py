from abc import ABC, abstractmethod
from typing import final


class Display(ABC):
    @abstractmethod
    def get_columns(self) -> int:
        pass

    @abstractmethod
    def get_rows(self) -> int:
        pass

    @abstractmethod
    def get_row_text(self, row: int) -> str:
        pass
    
    @final
    def show(self) -> None:
        for i in range(self.get_rows()):
            print(self.get_row_text(i))