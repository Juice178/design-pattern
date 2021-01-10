class Memento:
    def __init__(self, money: int) -> None:
        self.money = money
        self.fruits = []

    def get_moneny(self) -> int:
        return self.money

    def add_fruit(self, fruit: str) -> None:
        self.fruits.append(fruit)

    def get_fruits(self) -> list:
        return self.fruits.copy()