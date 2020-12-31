from border import Border
from display import Display
from string_buffer import StringBuffer


class FullBorder(Border):
    def __init__(self, display: Display):
        super().__init__(display)

    def get_columns(self) -> int:
        return 1 + self._display.get_columns() + 1

    def get_rows(self) -> int:
        return 1 + self._display.get_rows() + 1

    def get_row_text(self, row: int) -> str:
        if row == 0:
            return "+" + self._make_line("-", self._display.get_columns()) + "+"
        elif row == self._display.get_rows() + 1:
            return "+" + self._make_line("-", self._display.get_columns()) + "+"
        else:
            return "|" + self._display.get_row_text(row - 1) + "|"

    def _make_line(self, ch: str, count: int) -> str:
        buf = StringBuffer()
        for _ in range(count):
            buf.append(ch)
        return buf.to_string()