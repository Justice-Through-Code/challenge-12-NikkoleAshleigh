from book import Book


class Library():
    def __init__(self):
        """Initialize the empty book list"""
        self.books = []

    def add_title(self, title, author):
        """Add a Book object with the given title and author to the book list"""
        book = Book(title, author)

        self.books.append(book)

    def count_books(self):
        """Return the number of books currently in the booklist"""
        
        return len(self.books)

    def remove_title(self, title):
        """Remove a book from the book list"""
        
       
        # counter = 0
        # for book in self.books:
        #     if book.title == title:
        #         self.books.pop(counter)
        #     counter += 1

        for i, book in enumerate(self.books):
            if book.title == title:
                self.books.pop(i)
           

    def is_empty(self):
        """Return True if the book list is empty, False if not"""
        return self.books == []

    def display_books(self):
        for i in self.books:
            print(i) 