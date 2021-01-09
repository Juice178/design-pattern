from random_number_generator import RandomNumberGenerator
from digit_observer import DigitObserver
from graph_observer import GraphObserver

def main() -> None:
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observers(observer1)
    generator.add_observers(observer2)
    generator.execute()


if __name__ == "__main__":
    main()