from abc import ABC, abstractmethod
from number_generator import NumberGenerator


class Observer:
    @abstractmethod
    def update(self, generator: NumberGenerator) -> None:
        pass