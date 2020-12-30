from display import Display


class StringDisplay(Display):
    def __init__(self, string):
        self._string = string
    
    def get_columns(self) -> int:
        return len(self._string.encode('utf-8'))

    def get_rows(self) -> int:
        return 1

    def get_row_text(self, row: int) -> str:
        if row == 0:
            return self._string
        else:
            return None