import sys, os
from pathlib import Path
path = Path(os.path.dirname(os.path.abspath(__file__)))
parent_path = str(path.parent) + '/'
sys.path.append(parent_path)
from framework import Product


class IDCard(Product):
    def __init__(self, owner):
        print(f"Create {owner}'s card. '")
        self.owner = owner

    def use(self):
        print(f"Use {self.owner}'s card. '")

    def get_owner(self):
        return self.owner