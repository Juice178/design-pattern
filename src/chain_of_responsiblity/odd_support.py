from support import Support
from trouble import Trouble


class OddSupport(Support):
    def __init__(self, name: str):
        super().__init__(name)

    def resolve(self, trouble: Trouble) -> bool:
        if trouble.get_number() % 2 == 1:
            return True 
        else:
            return False
