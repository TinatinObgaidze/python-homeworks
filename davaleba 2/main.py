# 1 if the first number is larger than the second, display the second one first, otherwise show the first number first

x = int(input("Enter the first number :  "))
y = int(input("Enter  the second number :  "))
if x > y:
    print(y, x)
else:
    print(x, y)

# 2 enter a number under 20. if entered number is 20 or more, display the msg "too high", otherwise "thank you"

x = int(input("enter a number under 20:   "))
if x >= 20:
    print("Too high")
else:
    print("Thank you")

# 3 enter a number between 10 and 20 (inclusive).if they enter a number within this range,
# display "Thank you", otherwise "incorrect answer"

x = int(input("enter a number between 10 and 20:   "))
if 10 <= x <= 20:
    print("Thank you")
else:
    print("Incorrect answer")

# 4
colour = str(input("What is your favorite colour? \t"))
if colour == 'red':
    print("I like red too")
else:
    print("I don't like", colour, "i prefer red")

# 5
answer = str(input("is it raining? \t"))
print(str.lower(answer))
if answer == 'yes':
    print(input("is it windy? \t"))
    if answer == 'yes':
        print("it is too windy for an umbrella")
    else:
        print("Take an umbrella")

# 6
age = int(input("enter your age:   "))
if age >= 18:
    print("you can vote")
    if age == 17:
        print("you can learn to drive")
        if age == 16:
            print("you can buy a lottery ticket")
else:
    print("you can go trick-or-treating")

# 7
number = int(input("enter a number: \n"))
if number < 10:
    print("too low")
elif 10 < number < 20:
    print('Correct')
else:
    print("too high")

# 8
num = int(input("enter 1, 2 or 3 :    "))
if num == 1:
    print("Thank you")
elif num == 2:
    print("Well done")
else:
    print("Error message")

# 9
is_hot = False
is_cold = False
if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day")


