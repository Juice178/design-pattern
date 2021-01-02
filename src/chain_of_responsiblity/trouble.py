class Trouble:
    def __init__(self, number: int) -> None:
        self._number = number
    
    def get_number(self) -> int:
        return self._number

    def __str__(self) -> str:
        return f"[Trouble {self._number} ]"