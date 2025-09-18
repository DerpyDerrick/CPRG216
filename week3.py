# This is our 3rd class demo
'''
In this class we will work on variables, 
operators and other stuff
'''
# Review
# assignment
i = 7 # int
f = 6.9 # float
text = "Hello" # String
condition = True # Bool

print("The value of variable i is:" ,i," and the type is ",type(i))
print("The value of variable f is:" ,f," and the type is ",type(f)) 
print("The value of variable text is:" ,text," and the type is ",type(text)) 
print("The value of variable condition is:" ,condition," and the type is ",type(condition))
# some function call : print, input, int, float, str, bool
num_as_text = "43"

num_as_num = int(num_as_text) # converting string (text) to num

print(num_as_text) # will print as a text
print(num_as_num) # will it print???
print(str(num_as_num)) #equivalent
num = 3
num_f = float(3)
num2 = 3.4
num2_i = int(num2)
num2_as_text = str(num2)
'''
# Using input function.. Note input function always return a string (text)

user_input = int(input("Please enter your year of birth\n"))
print("Your age is", 2025 - user_input)

'''

# print function
    # working with a serparator

print("Hello", "world", sep=' ', end =' ')
print("Hello", "world", sep=' ')
print("Hello\tworld")
print("Hello\nworld")
print('What is the student\'s name?')
print('Use this symbol \\ to make an escape character')


# precedence rules

expression = 3+4*0-300+12/3
print(expression)

expression = 4/2*3

# More about Assignment

x = 3
x = x + 5

print(x)

# can we have a shorthand for this expression?\

x += 5 # x = x + 5
print(x)
# other expressions
print(x)
x -= 2 # x = x - 2
print(x)
x *= 3 # x = x * 3
print(x)
x /= 2 # x = x / 2
print(x)
x **= 4 # x = x**4
print(x)

