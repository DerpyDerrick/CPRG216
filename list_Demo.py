numbers = [1, 2, 3, 4, 5, 6]
num = 2
week = ['Sat', 'Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri']

print(week)
print(numbers)
print(num)

for day in week:
    print(day)

for number in numbers:
    square = number
    square = square**2
    print(square)

gpas = [2,3,4]
gpas.append(3.4)
sum = 0
for gpa in gpas:
    sum += gpa
    print(gpa)