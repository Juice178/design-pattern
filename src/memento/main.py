from game import Gamer, Memento
from time import sleep


def main() -> None:
    gamer = Gamer(100)
    memento = gamer.create_memento()
    for i in range(100):
        print(f"==== {i}")
        print(f"Current state: {gamer}")

        gamer.bet()

        print(f"Current money is: {gamer.get_moneny()}")

        if gamer.get_moneny() > memento.get_moneny():
            print("Keep current money")
            memento = gamer.create_memento()
        elif gamer.get_moneny() < memento.get_moneny():
            print("Rever to the previous condition")
            gamer.restore_memnto(memento)

        try:
            sleep(1)
        except KeyboardInterrupt:
            print("")
    
if __name__ == "__main__":
    main()