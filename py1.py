class Book:
    def __init__(self, book_title, book_author, book_pages):
     self.title = book_title
     self.author = book_author
     self.pages = book_pages

book = Book('Animal Farm', 'George Orwell', 100)
print(book.title)

class Car:
    def __init__(self, car_color, car_make, car_model):
        self.tires = '4'
        self.color = car_color
        self.make = car_make
        self.model = car_model

car = Car('blue', 'ford','focus')
print(car.tires)