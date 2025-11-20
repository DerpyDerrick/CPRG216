# Function One
def max(x,y,z):
    if x > y: # if first number is greater than second number
        if x > z: # if first number is greater than third number
            return x
        else: #third is greater than first
            return z
    else: # second is greater than first
        if y > z: 
            return y #second is greater than third
        else:
            return z #third is greatest
# Testing
print(max(1,2,3))
print(max(2,1,3))
print(max(3,2,1))
print(max(3,1,2))
print(max(1,3,2))
print(max(2,3,1))


# Function Two
def person(name, birth):
    print("Welcome ",name,", you are ",2025-birth," years old.",sep="")
# Testing
person("me",2007)
person("myself",2020)
person("I",1999)


# Function Three
def sqrt(x):
    x**=0.5
    print(x)
    return(x)
# Testing
sqrt(4)
sqrt(16)
sqrt(64)
sqrt(2.56)