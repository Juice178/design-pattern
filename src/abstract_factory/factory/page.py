from abc import ABC, abstractmethod

class Page(ABC):
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._content = []

    def add(self, item):
        self._content.append(item)

    def output(self):
        filename = f"{self._title}.html"
        with open(filename, "w") as f:
            f.write(self.make_html())
        print(f"{filename} is created.")
    
    @abstractmethod
    def make_html(self):
        pass
        