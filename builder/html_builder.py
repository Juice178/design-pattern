from builder import Builder

class HTMLBuilder(Builder):
    def __init__(self):
        self._filename = None
        self._writer = None

    def make_title(self, title):
        self._filename = title + ".html"
        self._writer = open(self._filename)
        self._writer.write(f"<html><head><title>{title}</title></head><body>\n")
        self._writer.write(f"<h1>{title}</h1>\n")
    
    def make_string(self, string):
        self._writer.write(f"<p>{string}</p>\n")
    
    def make_items(self, items):
        self._writer.write("<ul>")
        for i in range(len(items)):
            self._writer.write(f"<li>{items[i]}</li>\n")
        self._writer.write("</ul>\n")

    def close(self):
        self._writer.write("</body></html>\n")
        self._writer.close()
    
    def get_result(self):
        return self._filename
