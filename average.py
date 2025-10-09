print("Welcome to the average calculation program")

while True:
    print("Please enter three numbers.")
    a = float(input(""))
    b = float(input(""))
    c = float(input(""))

    sum = a+b+c
    average = sum/3

    print("The average is", average)
    user = input("Do you want to continue? ")
    user = user.lower()
    if user == "no" :
        break
    elif user == "n" :
        break
