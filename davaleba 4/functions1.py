def funcion1():
    print("aaah")
    print("aaah 2")
print("this is outside the function")
funcion1()

def function2(x):
    return 2 * x
a = function2(3)
print(a)
b = function2(4)
print(b)

def function3(x, y):
    return x + y
e = function3(1, 2)
print(e)

def fun4(x):
    print(x)
    print("still in this fun")
    return  3 * x
f = fun4(4)
print(f)

def fun5(some_arg):
    print(some_arg)
    print("weee")
fun5("traki")


#bmi calculator

name1 = 'yk'
height_ml = 2
weight_kgl = 90

name2 = "yk's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "yk's brother"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print(("bmi :  "))
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + "is overweight"
result1 = bmi_calculator(name1, height_ml, weight_kgl)
result2 = bmi_calculator(name2,height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)
print(result1)
print(result2)
print(result3)

def km(miles):
    km_1 = 1.6 * miles
    return km_1
km_2  = km(float(input("enter miles here :          ")))
print(km_2)
