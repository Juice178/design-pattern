from aggregate import Aggregate
from book import Book
import bookshelf_iterator as bsi


class BookShelf(Aggregate):
    def __init__(self, max_size):
        self.books = [0] * max_size
        self.last = 0

    def get_book_at(self, index):
        return self.books[index]

    def append_book(self, book):
        self.books[self.last] = book
        self.last += 1

    def get_length(self):
        return self.last

    def iterator(self):
        return bsi.BookShelfIterator(self)
    