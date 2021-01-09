from game.memento import  Memento
import random


class Gamer:
    fruits_name = ["Apple", "Grape", "Bananna", "Orange"]
    def __init__(self, money: int) -> None:
        self._money = money
        self._fruits = []
        
    def get_moneny(self) -> int:
        return self._money

    def bet(self) -> None:
        dice = random.randint(1, 6)
        if dict == 1:
            self._money += 100
            print("Money is increased.")
        elif dice == 2:
            self._money /= 2
            print("Money is halved.")
        elif dice == 6:
            fruit = self.get_fruit()
            print(f"Got fruit: {fruit}")
            self._fruits.append(fruit)
        else:
            print("Nothing happend...")

    def create_memento(self) -> Memento:
        m = Memento(self._money)
        it = iter(self._fruits)
        while (fruit := next(it, None)) is not None:
            if fruit.startswith("good"):
                m.add_fruit(fruit)
        return m

    def restore_memnto(self, memento: Memento) -> None:
        self._money = memento.money
        self._fruits = memento.get_fruits()

    def __str__(self) -> str:
        return f"[money = {self._money}, fruits = {self._fruits} ]"

    def get_fruit(self) -> str:
        prefix = ""
        if bool(random.getrandbits(1)):
            prefix = "good"
        return prefix + self.fruits_name[random.randint(0, len(self.fruits_name)-1)]
