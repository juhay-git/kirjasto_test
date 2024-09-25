class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {"title": title, "author": author}
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book["title"] != title]

    def list_books(self):
        return [book["title"] for book in self.books]