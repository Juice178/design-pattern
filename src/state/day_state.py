from state import State
# from night_state import NightState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context import Context


class DayState(State):
    _singleton = None
    _has_created_before = False

    def __init__(self):
        print("hi")
        if not self._has_created_before:
            self.create_instance()
            self.update()
            print("An instance is created.")
        return self._singleton

    @classmethod
    def update(cls):
        cls._has_created_before = True

    @classmethod
    def create_instance(cls):
        cls._singleton = DayState()
    
    @classmethod
    def get_instance(cls) -> State:
        # cls.create_instance()
        return DayState()

    def do_clock(self, context: 'Context', hour: int) -> None:
        from night_state import NightState
        if hour < 9 or 17 <= hour:
            context.change_state(NightState.get_instance())

    def do_use(self, context: 'Context') -> None:
        context.record_log("Using a safe (day)")

    def do_alarm(self, context: 'Context') -> None:
        context.call_secruity_center("Emergency Alarm (day)")

    def do_phone(self, context: 'Context') -> None:
        context.call_secruity_center("Normal call (day)")

    def __str__(self) -> str:
        return "[day]"

    

