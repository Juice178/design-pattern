from pagemaker.writer import Writer, FileWriter


class HtmlWriter:
    def __init__(self, writer: Writer) -> None:
        self._writer = writer
    
    def title(self, title: str) -> None:
        self._writer.write("<html>")
        self._writer.write("<head>")
        self._writer.write(f"<title>{title}</title>")
        self._writer.write("</head>")
        self._writer.write("<body>\n")
        self._writer.write(f"<h1>{title}</h1>\n")

    def paragraph(self, msg: str) -> None:
        self._writer.write(f"<p>{msg}</p>\n")

    def link(self, href: str, caption: str) -> None:
        self.paragraph(f"<a href='{href}'>{caption}</a>")

    def mailto(self, mailaddr: str, username: str) -> None:
        self.link(f"mailto: {mailaddr}", username)

    def close(self) -> None:
        self._writer.write("<body>")
        self._writer.write("</html>\n")
        self._writer.close()
    
    