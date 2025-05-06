# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

#  solution

class Book:
    total_books = 0 
    def __init__(self , tital , author):
        self.tital = tital
        self.author = author
        self.incrment_book_count()
        print(f"Book '{self.tital}' by {self.author} added.")
        

    @classmethod
    def incrment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
book1 = Book("Sono Tum Sitary ho", "Ghulam Ali")
book2 = Book("Aasman se gira", "Ghulam Ali")
book3 = Book("Tumhare liye", "Ghulam Ali")
book4 = Book("Tumhare liye", "Ghulam Ali")
print(Book.get_total_books())

