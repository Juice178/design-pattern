from printable import Printable
from printer import Printer

class PrinterProxy(Printable):
    def __init__(self, name: str) -> None:
        self._name = name
        self._real = None

    def set_printer_name(self, name: str) -> None:
        if self._real is not None:
            self._real.set_printer_name(name)
        self._name = name
    
    def get_printer_name(self) -> str:
        return self._name

    def print(self, string: str) -> None:
        self._realize()
        self._real.print(string)

    def _realize(self) -> None:
        if self._real is None:
            self._real = Printer(self._name)