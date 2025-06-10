class Product:
    def __init__(self, name="", price=0.0):
        self.name = name
        self.price = price
    def getDescription(self):
        return self.name

class Book(Product):
    def __init__(self, name="", price=0.0, author=""):
        Product.__init__(self, name, price)
        self.author = author
    def getDescription(self):
        return Product.getDescription(self) + " by " + self.author

class Movie(Product):
    def __init__(self, name="", price=0.0, year=0):
        Product.__init__(self, name, price)
        self.year = year
    def getDescription(self):
        return Product.getDescription(self) + " (" + str(self.year) + ")"
    
    
def display(product):
    print(product.getDescription())

book = Book("Catcher in the Rye", 9.99, "J. D. Salinger")
display(book)

product = Book("Catcher in the Rye", 9.99, "J. D. Salinger")
if isinstance(product, Product):
    print("This is a product.")
if isinstance(product, Movie):
    print("This is a movie.")
if isinstance(product, Book):
    print("This is a book.")