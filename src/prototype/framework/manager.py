from framework.product import Product


class Manager:
    _showcase = dict()

    def register(self, name, proto):
        self._showcase[name] = proto

    def create(self, protoname):
        p = self._showcase.get(protoname)
        return p.create_clone()


    