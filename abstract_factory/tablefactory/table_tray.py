from factory import Tray
from tablefactory.string_buffer import StringBuffer

class TableTray(Tray):
    def __init__(self, caption):
        super().__init__(caption)
    
    def make_html(self):
        buffer = StringBuffer()
        buffer.append("<td>")
        buffer.append("<table width='100%' border='1'><tr>")
        buffer.append(f"<td bgcolor='#cccccc' align='center colspan='{len(self._tray)}<b>{self._caption}</b></td>")
        buffer.append("</tr>\n")
        buffer.append("<tr>\n")
        for item in self._tray:
            buffer.append(item.make_html())
        buffer.append("</tr></table>")
        buffer.append("</td>")
        return buffer.to_string()