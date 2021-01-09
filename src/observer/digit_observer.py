from observer import Observer
from number_generator import NumberGenerator
from time import sleep


class DigitObserver(Observer):
    def __init__(self) -> None:
        super().__init__()

    def update(self, generator: NumberGenerator) -> None:
        print(f"DigitObserver: {generator.get_number()}")
        sleep(10)