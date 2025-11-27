class Car:
    def __init__(self, year, make, status, color, transmission, model, milage, body):
        self.year = year
        self.make = make
        self.status = status
        self.color = color
        self.transmission = transmission
        self.model = model
        self.milage = milage
        self.body = body

    def set_year(self, year):
        self.year = year
        
    def set_make(self, make):
        self.make = make

    def set_status(self, status):
        self.status = status
    
    def set_color(self, color):
        self.color = color
    
    def set_transmission(self, transmission):
        self.transmission = transmission
    
    
    def set_model(self, model):
        self.model = model
    
    
    def set_milage(self, milage):
        self.milage = milage
    
    
    def set_body(self, body):
        self.body = body