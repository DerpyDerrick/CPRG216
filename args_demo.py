def get_age(name, yob):
    print("Welcome", name)
    age = 2025-yob
    print("YUour age is ", age)

get_age("John", 2000)
get_age(yob = 2003, name = "Top")
# printq("Hello", "Wpr;d", ends"") incorrect


# default / optional args
def pow(x,y=2):
    print(x**y)




pow(2,3)
pow(3,2)

pow(4)

# demo of varibles in length args

def mysum(*nums):
    sum = 0
    for num in sum:
        sum+= num

    print(sum)
    return sum

mysum()
mysum(4)
mysum(4,18)