from bigchar import BigChar
from bigchar_factory import BigCharFactory


class BigString:
    def __init__(self, string: str) -> None:
        self._bigchars = [None] * len(string)
        factory = BigCharFactory.get_instance()
        for i in range(len(self._bigchars)):
            self._bigchars[i] = factory.get_bigchar(string[i])
        
    def print(self) -> None:
        for i in range(len(self._bigchars)):
            self._bigchars[i].print()
