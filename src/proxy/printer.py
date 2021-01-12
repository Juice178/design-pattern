from printable import Printable
from time import sleep

class Printer(Printable):
    def __init__(self, name: str) -> None:
        self._name = name
        self._heavy_job(f"Creating a Printer instance - {name}")

    def set_printer_name(self, name: str) -> None:
        self._name = name

    def get_printer_name(self) -> str:
        return self._name 

    def print(self, string: str) -> None:
        print(f"==={self._name}===")
        print(string)

    def _heavy_job(self, msg: str) -> None:
        print(msg, end="", flush=True)
        for _ in range(5):
            try:
                sleep(1)
            except InterruptedError:
                pass
            finally:
                print(".", end="", flush=True)
        print("Finished.")
    