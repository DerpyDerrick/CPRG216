print("Hello, welcome to the peart software..")
name = input("Please Enter your name:\n")
if name == 'hani':
    name = 'Hani'

print("Welcome, ", name)
print("To have a drink you need to provide your age")

age = int(input("What is your age?"))

is_adult = age >= 18

if is_adult:
    print("You are allowed to have a drink..")
else:
    print("Sorry, you are a child")

