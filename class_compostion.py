# class BookShelf:
#     def __init__(self, quantity):
#         self.quantity = quantity
    
#     def __str__(self):
#         return f"Bookshelf with {self.quantity} books."
class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."

#shelf = BookShelf(300)

#print(shelf)

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter")
book1 = Book("Python")
shelf = BookShelf(book, book1)
print(shelf)

#Inheritance means that book is a bookshelf
#while, Composition means that a bookshelf has many books 