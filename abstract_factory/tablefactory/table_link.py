from factory import Link

class TableLink(Link):
    def __init__(self, caption, url):
        super().__init__(caption, url)
    
    def make_html(self):
        return f"<td><a href={self._url}>{self._caption}</a><td>\n"
