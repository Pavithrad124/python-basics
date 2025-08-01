class Library:
    def __init__(self):
        self.books = []

    def display_books(self):
        if self.books:
            print("Available books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books are available in the library.")

    def lend_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"The book '{book_name}' has been lent out.")
        else:
            print(f"Sorry, the book '{book_name}' is not available.")

    def get_book_count(self):
        # Returns the total number of books in the library
        return len(self.books)
        print(f"\nTotal books in the library: {my_library.get_book_count()}")

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"The book '{book_name}' has been added to the library.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"The book '{book_name}' has been returned to the library.")



my_library = Library()
my_library.add_book(input("Enter the book name: "))
my_library.display_books()
my_library.add_book(input("Enter the book name: "))
my_library.add_book(input("Enter the book name: "))
my_library.display_books()
my_library.lend_book(input("Enter the lend book name: "))
my_library.display_books()
my_library.return_book(input("Enter the return book name: "))
my_library.display_books()