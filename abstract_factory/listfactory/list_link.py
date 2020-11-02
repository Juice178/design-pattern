from factory import Link

class ListLink(Link):
    def __init__(self, caption, url):
        super().__init__(caption, url)
    def make_html(self):
        return f" <li><a href='{self._url}'>{self._caption}<a></li>\n"