class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
    def display(self):
        print(f"title {self.title} Author {self.author} ISBN{self.isbn}")
        
class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
        print(f"Book title {book.title} added to the library.")
    def remove_book(self,isbn):
        book_to_remove = None
        for book in self.books:
            if book.isbn == isbn:
                book_to_remove = book
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f" Book {book_to_remove.title} removed from library ")
    def display_books(self):
        if not self.books:
            print("No books")
        else:
            for book in self.books:
                book.display()
            

class SpecialLibrary(Library):
    def add_book(self, book):
        #Library.add_book(self, book)
        super().add_book(book)
        print(f"Special handling for book {book.title}")
book1 = Book("a","c","222")
book2 = Book("aa","cx","2222")

my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)
my_library.display_books()


my_library.remove_book("222")
my_library.display_books()
special_library = SpecialLibrary()
special_library.add_book(book1)
    