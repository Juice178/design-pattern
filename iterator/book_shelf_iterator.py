from iterator import Iterator
from book_shelf import BookShelfIterator

class BookShelfIterator(Iterator):
    def __init__(self, book_shelf):
        self.book_shelf = book_shelf
        self.index = 0

    @abstractmethod
    def has_next(self):
        if (self.index < self.book_shelf.get_length()):
            return True
        else:
            return False

    @abstractmethod
    def next(self):
        book = BookShelf.get_book_at(self.index)
        self.index += 1
        return book 

