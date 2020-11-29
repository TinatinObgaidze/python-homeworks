# 1
name = input("enter your name :    ")
for i in range(3):
    print(name)
# 2
name = input("enter your name:    ")
number = int(input("enter the number:      "))
for i in range(number):
    print(name)

# 3
name = input("enter your name :   ")
for i in name:
    print(i)

# 4
name = input("enter your name :    ")
number = int(input("enter the number :   "))
for x in range(number):
    for i in name:
        print(i)
# 5
number = int(input("enter a number between 1 and 12 :   "))
for i in range(1, 12):
    print(i)

# 6
x = int(input("enter a number below 50 :   "))
for i in range(50, x - 1, -1):
    print(i)

# 7
name = input("enter your name:   ")
number = int(input("enter the number :   "))
if number < 10:
    for i in range(0, number):
        print(name)
    else:
        print("too high")

# 8
total = 0
for i in range(0, 5):
    num = int(input("enter a number :  "))
    answer = input(" do you want this number included ?    (yes/no)  ")
    if answer == "yes":
        total += num
        print(total)

# 9
answer = input("which direction do you want to count?  up / down \n")
if answer == "up":
    num = int(input("enter the top number:  "))
    for i in range(1, num + 1):
        print(i)
elif answer == "down":
    num_1 = int(input("enter a number below 20 :  "))
    for i in range(20, num_1 - 1, -1):
        print(i)
    else:
        print("i don't understand")
# 10
people = int(input("how many people do you want to invite to a party? : \n"))
if people < 10:
    for i in range(0, people):
        names = (input("enter the names : \n  "))
        print(names, "has been invited")
else:
    print("too many people")