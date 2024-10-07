# Exercise 3: Library Management System 
# Create a Book class containing the following attributes: title, author, isbn
# The book class must contains the following methods:
# __str__ method to return a string representation of the book.
# @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". It means that you must use the class reference cls to create a new object of the Book class using a string.
# Example: 
# book = “La Divina Commedia, D. Alighieri, 999000666”
# divina_commedia: Book = Book.from_string(book)
# Here divina_commedia must contain an instance of the class Book with 
# title = La Divina Commedia, author = D. Alighieri, isbn = 999000666
# Create a Member class with the following attributes: name, member_id, borrowed_books
# The member class must contain the following methods:
# borrow_book(book) to add a book to the borrowed_books list.
# return_book(book) to remove a book from the borrowed_books list.
# __str__ method to return a string representation of the member.
# @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".
# Create a Library class with the following attributes: books, members, total_books (class attribute to keep track of the total number of books)
# The library class must contain the following methods:
# add_book(book) to add a book to the library and increment total_books.
# remove_book(book) to remove a book from the library and decrement total_books.
# register_member(member) to add a member to the library.
# lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.
# __str__ method to return a string representation of the library with the list of books and members.
# @classmethod library_statistics(cls) to print the total number of books.
# Create a script and play a bit with the classes:
# Create instances of books and members using class methods. Register members and add books to the library. Lend books to members and display the state of the library before and after lending.
class Book:
    total_books = 0
    def __init__(self,
                 title:str,
                 author:str,
                 isbn:int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

        Book.total_books += 1
    def __str__(self) -> str:
        return f'title : {self.title} , author : {self.author}, isbn : {self.isbn}'
    
    @classmethod
    def from_string(cls,book_str):
        params: list = book_str.split(",")
        return cls(params[0], params[1],params[2])

    @classmethod
    def library_statistics(cls):
        print (f'Libri totali: {cls.total_books}')
    
    
class Member:
    def __init__(self,
                 name :str,
                 id:int) -> None:
        self.name = name 
        self.id = id
        self.borrowed_books = []
        
    def borrow_book(self,book:Book):
        self.borrowed_books.append(book)
        
    def return_book(self,book):
        self.borrowed_books.remove(book)
        
    def __str__(self) -> str:
        return f'name : {self.name} , id : {self.id}'
    
    @classmethod
    def from_string(cls,member_str):
        params: list = member_str.split(",")
        return cls(params[0], params[1])
    
class Library:

    def __init__(self) -> None:
        self.books = []
        self.members = []
        
    def add_book(self,book):
        return self.books.append(book)
    
    def remove_book(self,book):
        return self.books.remove(book)
    
    def register_member(self,member):
        return self.members.append(member)
    
    def lend_book(self,book,member):
        if book in self.books :
            if member in self.members:
                self.remove_book(book)
                return f'Libro {book.title} prestato al membro {member.name}'
            return f'Membro non registrato'
        return f'Libro non disponibile'
    
    def __str__(self) -> str:
        return f'Lista libri : {self.books} ,\nLista membri : {self.members}'
    
    
    
    
book1 = Book(title='Python', author='George Orwell',isbn= 1234567890)
book2 = Book(title='To Kill a Mockingbird', author='Harper Lee',isbn= 2345678901)
book3 = Book(title='The Great Gatsby', author='F. Scott Fitzgerald', isbn=3456789012)
member1 = Member(name='John Doe', id=1)
member2 = Member(name='Jane Doe', id=2)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

(Book.library_statistics())

library.register_member(member1)
library.register_member(member2)

print(library.lend_book(book1, member1)) #libro prestato
print(library.lend_book(book1, member2)) #libro non disponibile
new_member = Member(name='Jack Smith',id=3) 
print(library.lend_book(book2, new_member)) #membro non registrato


print(member1)
print(member2)

library.add_book(book1)

(Book.library_statistics())

print(library)

    
            
            
            
        