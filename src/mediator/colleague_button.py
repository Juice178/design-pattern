from colleague import Colleague
from mediator import Mediator
from PyQt5.QtWidgets import QPushButton

class Meta(type(QPushButton), type(Colleague)):
    pass


class ColleagueButton(QPushButton, Colleague,  metaclass=Meta):
    def __init__(self, caption: str) -> None:
        super().__init__(caption)

    def set_mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

    def set_colleague_enabled(enabled: bool) -> None:
        self.setEnabled(enabled)
