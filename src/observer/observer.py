from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from number_generator import NumberGenerator


class Observer:
    @abstractmethod
    def update(self, generator: 'NumberGenerator') -> None:
        pass