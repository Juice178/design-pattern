import sys, os
from pathlib import Path
path = Path(os.path.dirname(os.path.abspath(__file__)))
parent_path = str(path.parent) + '/'
sys.path.append(parent_path)
from framework import Product
from framework import Factory
from idcard import IDCard

class IDCardFactory(Factory):
    _owners = []

    def _create_product(self, owner):
        return IDCard(owner)

    def _register_product(self, product):
        self._owners.append(product.get_owner())

    def get_owners(self):
        return self._owners

