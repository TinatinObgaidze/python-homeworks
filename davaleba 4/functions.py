def is_even(i):
    if i % 2 == 0:
        return True
    else:
        return False


value = is_even(5)
print(value)


def hello_twice():
    print('hello')
    print('hello')


hello_twice()


def print_twice():
    print('hello')
    print("hello")


print_twice()


def average_num(a, b):
    res = (a + b) / 2
    return res


y = 3
z = 5
x = average_num(y + 1, z)
print(x)


def number(a=0, b=0):
    res = (a + b) / 2
    return res


x = number()
print(x)
x = number(2)
print(x)
x = number(2, 8)
print(x)

double = lambda x: x * 2 % 5
print(double(12))


def double(x):
    return x * 2 % 5


print(double(6))


# 1
def averg(a, b):
    jami = (a + b) / 2
    return jami


x = averg(15, 541)
print(x)
x = averg(14, 56)
print(x)
x = averg(13, 81)
print(x)


def sashualo(a, b):
    gamotvla = (a + b) / 2
    return gamotvla


x = sashualo(2, 5)
print(x)


# 3
def cube(a):
    xarisxi = a ** 3
    return xarisxi


x = cube(5)
print(x)
x = cube(7)
print(x)
x = cube(1)
print(x)

# 4
import random


def minimaluri(a, b):
    minimaluri_1 = min(a, b)
    return minimaluri_1


a = random.randint(0, 10)
b = random.randint(0, 10)
print(minimaluri(a, b))


# 5
def is_odd(x):
    if x % 2 == 1:
        return True
    else:
        return False


print(is_odd(5))
print(is_odd(18))

# 6
from math import factorial


def factoriali(a):
    factoriali_1 = factorial(a)
    return factoriali_1


a = factoriali(4)
print(a)
a = factorial(7)
print(a)

# 7
import math


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


num = 4
print("factorial of ", num, 'is', factorial(num))


# 8
def dabechde():
    print('hello world')


dabechde()

# 9
kubi = lambda n: n ** 3
print(kubi(4))


# 10
def simple_num(x):
    if x == 2:
        return "martivia"
    elif x % 2 == 1:
        return "martivia"
    else:
        return "ar aris martivi"


x = 55
print(simple_num(x))
x = 64
print(simple_num(x))
x = 2
print(simple_num(x))
