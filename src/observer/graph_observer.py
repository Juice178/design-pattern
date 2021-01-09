from observer import Observer
from number_generator import NumberGenerator
from time import sleep


class GraphObserver(Observer):
    def __init__(self) -> None:
        super().__init__()

    def update(self, generator: NumberGenerator) -> None:
        print(f"GraphObserver")
        count = generator.get_number()
        for _ in range(count):
            print("*", end="")
        print("")
        sleep(1)