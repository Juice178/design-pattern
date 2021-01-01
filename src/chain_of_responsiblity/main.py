from no_support import NoSupport
from limit_support import LimitSupport
from odd_support import OddSupport
from special_support import SpecialSupport
from trouble import Trouble


def main():
    alice = NoSupport("Alice")
    bob = LimitSupport("Bob", 100)
    charlie = SpecialSupport("Charlie", 429)
    diana = LimitSupport("Diana", 200)
    elmo = OddSupport("Elmo")
    fred = LimitSupport("Fred", 300)

    alice.set_next(bob).set_next(charlie).set_next(diana).set_next(elmo).set_next(fred)

    for i in range(0, 500, 33):
        alice.support(Trouble(i))

if __name__ == "__main__":
    main()