from factory import Tray
from listfactory.string_buffer import StringBuffer

class ListTray(Tray):
    def __init__(self, caption):
        super().__init__(caption)
    
    def make_html(self):
        buffer = StringBuffer()
        buffer.append("<li>\n")
        buffer.append(f"{self._caption}\n")
        buffer.append("<ul>\n")
        for item in self._tray:
            buffer.append(item.make_html())
        buffer.append("</ul>\n")
        buffer.append("</li>\n")
        return buffer.to_string()
        


