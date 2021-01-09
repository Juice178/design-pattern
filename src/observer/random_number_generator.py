from number_generator import NumberGenerator
import random


class RandomNumberGenerator(NumberGenerator):
    def __init__(self) -> None:
        super().__init__()
        # self._random = None
        self._number = None

    def get_number(self) -> int:
        return self._number

    def execute(self):
        for _ in range(20):
            self._number = random.randint(0, 49)
            self.notify_observers()
