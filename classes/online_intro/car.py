class Car:
# Attributes
# functionalities (methods)
    make = 'bmw'
    year = 2020
    milage = 20000
    color = 'black'

    def __init__(self, make, year_value, mil, color):
        self.make = make
        self.year = year_value
        self.milage = mil
        self.color = color

    def set_make(self, make):
        self.make = make
        
    def set_color(self, value):
        self.make = value
