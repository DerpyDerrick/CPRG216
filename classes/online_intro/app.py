from online_intro.car import *

x = 2
y = 3.4
print(type(x), type(y))

c1 = Car('BMW', 2023, 20000, 'Silver') # we have to set everything here when we construuct the object
c2 = Car('Honda', 2025, 1000, 'Black')
c3 = Car('Kia', 2021, 30000, 'Blue')
c4 = Car('Jeep', 2020, 40000, 'Black')
print(c1.color, c1.make, c1.milage, c1.year)
print(c2.color, c2.make, c2.milage, c2.year)
print(c3.color, c3.make, c3.milage, c3.year)
print(c4.color, c4.make, c4.milage, c4.year)