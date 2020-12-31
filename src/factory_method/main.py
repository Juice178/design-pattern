from framework import Product, Factory
from idcard import IDCard, IDCardFactory


def main():
    factory = IDCardFactory()
    card1 = factory.create("Kenta")
    card2 = factory.create("test-user")
    card3 = factory.create("Mr X")
    card1.use()
    card2.use()
    card3.use()
    print(f"Registered owners are {factory.get_owners()}")

if __name__ == "__main__":
    main()
