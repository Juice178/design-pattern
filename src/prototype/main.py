from framework import Manager
from framework import Product
from message_box import MessageBox
from underline_pen import UnderlinePen
from copy import copy

def main():
    manager = Manager()
    upen = UnderlinePen('~')
    mbox = MessageBox('*')
    sbox = MessageBox('/')
    manager.register("strong message", upen)
    manager.register("warning box", mbox)
    manager.register("slash box", sbox)

    p1 = manager.create("strong message")
    assert isinstance(p1, Product)
    p1.use("Hello, world.")
    p2 = manager.create("warning box")
    assert isinstance(p2, Product)
    p2.use("Hello, world.")
    p3 = manager.create("slash box")
    assert isinstance(p3, Product)
    p3.use("Hello, world.")

if __name__ == "__main__":
    main()

    