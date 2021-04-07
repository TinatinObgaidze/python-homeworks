"""ამოიღეთ ფესვი 225625 დან და 4225 დან"""
print("by using sqrt() function:\n")
import math
number = 225625
number1 = 4225
print(f"The root of {number} is {math.sqrt(number)}")
print(f"The root of {number1} is {math.sqrt(number1)}\n")
print("by using loops:\n")
n = 225625
n1 = 4225
x = 0
y= 0
for i in range(n):
    x+=1
    if x ** 2 == n:
        print(f"The root of {n} is {x}")
for j in range(n1):
    y+=1
    if y ** 2 == n1:
        print(f"The root of {n1} is {y}")