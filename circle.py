# I want to compute the circum and the area of the circle
# assume the circle radius is 5
# modify : ask the user to enter the circle radius
# and that pi = 3.14

PI = 3.14
#PI = 1313.22 # logical error, cause if you want pi to be constant, it has to be unchanged and constant
user_input = input("Please enter the radius of the circle:")
print("Type of user input", type(user_input))
r = int(user_input)
circum = 2 * PI * r
area = PI * r **2
print(circum)
print(area)