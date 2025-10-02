user_input = int(input("Please enter a number you want the factorial of:"))
sum = 1
count = 0

if(user_input == 0):
    print("Factorial of 0 is 1")
elif(user_input < 0):
    print("You cannot input a negative number")
else:
    while count <= user_input :
        sum *= count
        count += 1
    print("The factorial of", user_input, "is:", sum)