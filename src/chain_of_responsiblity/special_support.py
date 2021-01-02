from support import Support
from trouble import Trouble


class SpecialSupport(Support):
    def __init__(self, name: str, number: int) -> None:
        super().__init__(name)
        self._number = number 
    
    def resolve(self, trouble: Trouble) -> bool:
        if trouble.get_number() == self._number:
            return True 
        else:
            return False
