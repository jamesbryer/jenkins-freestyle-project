'''
Create a class Book. Each book object should have the attributes: 
- title
- author (default unknown) 
- number of pages
- genre
- ISBN. 
The class should define the following methods:
- __init__ to set the attributes described above
- __str__ to print a description of the book
- a search method which returns all books by a given author (requires tracking of objects) - if there are no books by the given author return an empty list
- a method to check the validity of a given ISBN-13 - should return true if the ISBN is valid, false otherwise
As an additional stretch goal, create 2 subclasses for specific 
genres and override the __init__ method and __str__ methods appropriately
'''


class Book():
    books = []

    def __init__(self, title, pages, isbn, genre, author="Unknown"):
        '''
        A method to initialize a book object with a title, number of pages, ISBN, genre, and author
        '''
        self.title = title
        self.pages = pages
        self.isbn = isbn
        self.genre = genre
        self.author = author
        Book.books.append(self)

    @staticmethod
    def valid_isbn(isbn):
        '''
        A method to check the validity of a given ISBN-13 - should return true if the ISBN is valid, false otherwise
        '''
        isbn = isbn.replace("-", "")

        if not isbn.isdigit() or len(isbn) != 13:
            return False

        check_digit = int(isbn[-1])
        isbn = isbn[:-1]

        # Repeating pattern of weights [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
        weight = [1, 3] * 6
        digits_sum = sum(int(digit) * w for digit, w in zip(isbn, weight))
        check_sum = (10 - digits_sum % 10) % 10

        return check_sum == check_digit

    @staticmethod
    def search(author):
        '''
        A method to search for all books by a given author
        '''
        books_by_author = []

        for book in Book.books:
            if book.author == author:
                books_by_author.append(book)
        return books_by_author
    
    @staticmethod
    def search_book(title):
        '''
        A method to search for a single book by title
        '''
        for book in Book.books:
            if book.title == title:
                return book
            else:
                return "Book not found!"

    def __str__(self):
        '''
        A method to print a description of the book
        '''
        output = "Title:", self.title, "Author:", self.author, "Genre:", self.genre, "Number of Pages:", self.pages, "ISBN:", self.isbn
        return output
