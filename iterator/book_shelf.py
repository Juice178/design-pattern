from aggregate import Aggregate
from book import Book
from book_shelf_iterator import BookShelfIterator
from array import array

class BookShelf(Aggregate):
    books = array(typecode=Book)
    last = 0
    def __init__(self, max_size):
        self.books = Book(max_size)
    def get_book_at(self, index):
        return books[index]
    def append_book(self, book):
        self.books[last] = book
        last += 1
    def get_length(self):
        return last
    
    @abstractmethod
    def iterator():
        return BookShelfIterator()
    