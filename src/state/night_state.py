from state import State
from day_state import DayState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context import Context


class NightState(State):
    _singleton = None
    _has_created_before = False

    def __init__(self) -> None:
        if not self._has_created_before:
            self.create_instance()
            self.update()
            print("An instance is created.")

    @classmethod
    def update(cls):
        cls._has_created_before = True

    @classmethod
    def create_instance(cls):
        cls._singleton = cls()
    
    @classmethod
    def get_instance(cls) -> State:
        return cls._singleton 

    def do_clock(self, context: 'Context', hour: int) -> None:
        if 9 <= hour or hour < 17:
            context.change_state(DayState.get_instance())

    def do_use(self, context: 'Context') -> None:
        context.record_log("Using a safe (night)")

    def do_alarm(self, context: 'Context') -> None:
        context.call_secruity_center("Emergency Alarm (night)")

    def do_phone(self, context: 'Context') -> None:
        context.call_secruity_center("Normal call (night)")

    def __str__(self) -> str:
        return "[night]"