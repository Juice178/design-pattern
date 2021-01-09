from abc import ABC, abstractmethod
from observer import Observer


class NumberGenerator:
    def __init__(self) -> None:
        self._observers = []

    def add_observers(self, observer: Observer) -> None:
        self._observers.append(observer)

    
    def delete_observers(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        it = iter(self._observers)
        while (observer := next(it, None)) is not None:
            observer.update(self)
    
    @abstractmethod
    def get_number(self) -> int:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass
