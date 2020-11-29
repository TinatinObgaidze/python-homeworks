import math

# 1
num = float(input("enter a number with lots of decimal places: "))
print(num * 2)
print(round(num, 2))

# 2
num_1 = int(input("enter an integer that is over 500:   "))
answer = math.sqrt(num_1)
print(round(answer, 2))

# 3
print(round(math.pi, 5))

# 4
r = float(input("enter the radius of a circle :   "))
area = math.pi * r ** 2
print(area)

# 5
r_1 = float(input("enter the radius of cylinder:  \t"))
d = float(input("enter the depth of cylinder:  \t"))
area = math.pi * r_1 ** 2
volume = area * d
print(round(volume, 3))

# 6
number = int(input("enter the first number:    "))
number_1 = int(input("enter the second number :    "))
x = number // number_1
y = number % number_1
print(number, 'divided by', number_1, 'is', x, 'with', y, 'remaining')

# 7
square = 1
triangle = 2
n = int(input("choose a number 1 or 2:    "))
if n == 1:
    length = float(input("enter the length of its sides: \t"))
    area = length ** 2
    print(area)
elif n == 2:
    base = float(input("enter the base of  the triangle: \t"))
    height = float(input("enter the height of the triangle: \t"))
    area_1 = (base * 0.5) * height
    print(area_1)
else:
    print("suitable error message")


