from bookshelf import BookShelf
from book import Book
from iterator import Iterator

def main():
    """
    Put 4 books in a bookshelf and print a book name iteratively. 
    """
    bookshelf = BookShelf(4)
    bookshelf.append_book(Book("Around the World in 80 Days"))
    bookshelf.append_book(Book("Bible"))
    bookshelf.append_book(Book("Cinderella"))
    bookshelf.append_book(Book("Daddy-Long-Legs"))
    it = bookshelf.iterator()
    assert isinstance(it, Iterator) == True
    while (it.has_next()):
        book = it.next()
        print(book.get_name())


if __name__ == "__main__":
    main()