from factory import Page
from tablefactory.string_buffer import StringBuffer

class TablePage(Page):
    def __init__(self, title, author):
        super().__init__(title, author)
    
    def make_html(self):
        buffer = StringBuffer()
        buffer.append(f"<html><head></title>{self._title}</title></head>\n")
        buffer.append("<body>\n")
        buffer.append(f"<h1>{self._title}</h1>\n")
        buffer.append(f"<table width='80% border='3'>\n")
        buffer.append("<body>\n")
        for item in self._content:
            buffer.append(f"<tr>{item.make_html()}</tr>")
        buffer.append("</table>\n")
        buffer.append(f"<hr><address>{self._author}</address>")
        buffer.append("</body></html>\n")
        return buffer.to_string()
