from support import Support
from trouble import Trouble

class NoSupport(Support):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def resolve(self, trouble: Trouble) -> bool:
        return False



    