class library:
    books=['a','b','c','d','e']
    def __init__(self):
        print("welcome:")
    def display_books(self):
        print(self.books)
    def lend_book(self,book_name):

        self.books.remove(book_name)

    def add_book(self,book_name):
        self.books.append(book_name)
    def return_book(self, book_name):
        self.books.append(book_name)
obj=library()
obj.display_books()
obj.lend_book("Em")
obj.display_books()
obj.add_book()
obj.display_books()






