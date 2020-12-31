from border import Border
from display import Display


class SideBorder(Border):
    def __init__(self, display: Display, ch: str):
        super().__init__(display)
        self._border_char = ch

    def get_columns(self) -> int:
        return 1 + self._display.get_columns() + 1

    def get_rows(self) -> int:
        return self._display.get_rows()

    def get_row_text(self, row: int) -> str:
        return self._border_char + self._display.get_row_text(row) + self._border_char

