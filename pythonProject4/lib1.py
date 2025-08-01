class Library:
    def __init__(self):
        self.books = []

    def display_books(self):
        # Display the available books in the library and the count
        if self.books:
            print("Available books in the library:")
            for book in self.books:
                print(f"- {book}")
            print(f"\nTotal books in the library: {len(self.books)}")
        else:
            print("No books are available in the library.")

    def lend_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"The book '{book_name}' has been lent out.")
        else:
            print(f"Sorry, the book '{book_name}' is not available.")

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"The book '{book_name}' has been added to the library.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"The book '{book_name}' has been returned to the library.")

    def get_book_count(self):
        # Returns the total number of books in the library
        return len(self.books)


# Test the Library class
my_library = Library()

# Adding books to the library
book1 = input("Enter the book name to add: ")
my_library.add_book(book1)

# Display books after adding one
my_library.display_books()

book2 = input("Enter another book name to add: ")
my_library.add_book(book2)

book3 = input("Enter yet another book name to add: ")
my_library.add_book(book3)

# Display books after adding more
my_library.display_books()

# Lend a book
lend_book_name = input("Enter the book name to lend: ")
my_library.lend_book(lend_book_name)

# Display books after lending
my_library.display_books()

# Return a book
return_book_name = input("Enter the book name to return: ")
my_library.return_book(return_book_name)

# Display books after returning
my_library.display_books()

# Display total book count (using the new method)
print(f"\nTotal books in the library: {my_library.get_book_count()}")