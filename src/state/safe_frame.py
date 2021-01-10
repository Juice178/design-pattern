from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
from context import Context
from day_state import DayState
from night_state import NightState
from typing import TYPE_CHECKING
import sys

# if TYPE_CHECKING:
#     from day_state import DayState
#     from night_state import NightState

class SafelFrameMeta(type(QWidget), type(Context)):
    pass


class SafeFrame(QWidget, Context, metaclass=SafelFrameMeta):
    def __init__(self, title):
        super().__init__()
        self._title = title
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self._title)
        # Create textbox
        self.text_clock = QLineEdit(self)
        self.text_screen = QLineEdit(self)
        # self.textbox.move(20, 20)
        # self.textbox.resize(280,40)
        self.button_use = QPushButton('Use a safe', self)
        self.button_alarm = QPushButton('Emergecy Alarm', self)
        self.button_phone = QPushButton('Emergency call', self)
        self.button_exit = QPushButton('Exit', self)

        self._state = DayState.get_instance()
        print(self._state)
        lambda: self.action_performed('button_use')
        self.button_use.clicked.connect(lambda: self.action_performed('button_use'))
        self.button_alarm.clicked.connect(lambda: self.action_performed('button_alarm'))
        self.button_phone.clicked.connect(lambda: self.action_performed('button_phone'))
        self.button_exit.clicked.connect(lambda: self.action_performed('button_exit'))

    @pyqtSlot()
    def action_performed(self, button) -> None:
        if button == 'button_use':
            self._state.do_use(self)
        elif button == 'button_alarm':
            self._state.do_alarm(self)
        elif button == 'button_phone':
            self._state.do_phone(self)
        elif button == 'button_exit':
            sys.exit(0)
        else:
            print("?")

    def set_clock(self, hour: int) -> None:
        clock_string = "Current time is: "
        if hour < 10:
            clock_string += f"0 {hour}:00"
        else:
            clock_string += f"{hour}:00"
        print(clock_string)
        self._state.do_clock(self, hour)

    def change_state(self, state: 'State') -> None:
        print(f"{self._state} -> {state}")
        self._state = state

    def call_secruity_center(self, msg: str) -> None:
        print(f"Call {msg}")
    
    def record_log(self, msg: str) -> None:
        print(f"record ... {msg}")



