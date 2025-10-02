'''
Review of if statement
'''


# Now while loop
'''
- while : mandatory
- condition : mandatory
- the colon :
- one or more statements (indented)
'''
# True all the time

age = 19
is_adult = age >= 18

while is_adult: 
    print("The user is adult")
    age = 17
    is_adult = age >=18

# Example: print numbers from 1 to 10

num = 1

while num!=10:
    print(num)
    num += 1
