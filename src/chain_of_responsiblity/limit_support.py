from support import Support
from trouble import Trouble

class LimitSupport(Support):
    def __init__(self, name: str, limit: int):
        super().__init__(name)
        self._limit = limit 

    def resolve(self, trouble: Trouble) -> bool:
        if trouble.get_number() < self._limit:
            return True 
        else:
            return False
