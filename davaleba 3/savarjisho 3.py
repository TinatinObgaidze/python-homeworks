# 1
total = 0
while total <= 50:
    num = int(input("enter a number : "))
    total += num
    print("The total is", total)
    if total >= 50:
        break
# 2
num = 0
while num <= 5:
    num = int(input("enter a number :   "))
    if num > 5:
        print("the last number you entered was a", num)

# 3
number = int(input("enter a number :  "))
number_2 = int(input("enter a number :  "))
x = number + number_2
sum_1 = input("do you want to add another number ?  y/n \n ")
while sum_1 == "y":
    number_n = int(input("enter a number :  "))
    sum_1 = input("do you want to add another number ?  y/n \n")
    x += number_n
    if sum_1 != "y":
        break
    print(x)
# 4
answer = "y"
x = 0
while answer == "y":
    name = input("enter a name of somebody you want to invite :    ")
    print(name, "has now invited")
    x = x + 1
    answer = input("do you want to invite somebody else? y/ n \n")
    print("you have invite", x, "people")


