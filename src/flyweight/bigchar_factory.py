from __future__ import annotations
from bigchar import BigChar


class BigCharFactory:
    _singleton = None
    def __init__(self) -> None:
        self._pool = dict()
        if BigCharFactory._singleton == None:
            BigCharFactory._singleton = self

    @staticmethod
    def get_instance() -> BigCharFactory:
        BigCharFactory()
        return BigCharFactory._singleton

    def get_bigchar(self, charname: str) -> BigChar:
        bc = self._pool.get(charname, None)
        if bc == None:
            bc = BigChar(charname)
            self._pool[charname] = bc 
        return bc

    