
class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher Name:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        print("Publisher Name:", self.name)
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        super().display()
        print("Price:", self.price)
        print("Number of Pages:", self.no_of_pages)



p = Python("ABC Publications", "Python Programming",
           "LIJO", 450, 300)

print("Python Book Details")
p.display()
