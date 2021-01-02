from colleague import Colleague
from mediator import Mediator
from PyQt5.QtWidgets import QPushButton


class ColleagueButton(QPushButton, Colleague):
    def __init__(self, caption: str) -> None:
        super().__init__(caption)

    def set_mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

    def set_colleague_enabled(enabled: bool) -> None:
        self.setEnabled(enabled)
