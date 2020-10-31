from factory import Page
from listfactory.string_buffer import StringBuffer

class ListPage(Page):
    def __init__(self, title, author):
        super().__init__(title, author)
    
    def make_html(self):
        buffer = StringBuffer()
        buffer.append(f"<html><head><title>{self._title}</title></head>\n")
        buffer.append(f"<body>\n")
        buffer.append(f"<h1>{self._title}</h1>\n")
        buffer.append("<ul>\n")
        for item in self._content:
            buffer.append(item.make_html())
        buffer.append("</ul>\n")
        buffer.append(f"<hr><address>{self._author}</address>")
        buffer.append("</body></html>\n")
        return buffer.to_string()

