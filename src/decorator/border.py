from abc import ABC, abstractmethod
from display import Display


class Border(Display):
    def __init__(self, display: Display):
        self._display = display
    