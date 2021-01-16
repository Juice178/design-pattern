from state import State
# from night_state import NightState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context import Context


class DayState(State):
    _singleton = None

    def __init__(self):
      if DayState._singleton != None:
         raise Exception("This class is a singleton!")
      else:
         DayState._singleton = self

    @staticmethod
    def get_instance() -> State:
        if DayState._singleton == None:
            DayState()
        return DayState._singleton

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

    

