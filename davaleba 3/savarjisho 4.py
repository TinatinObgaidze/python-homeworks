import random
# 1
num = random.randint(1, 100)
print(num)

# 2
fruit = random.choice(["grape", "watermelon", "melon", "apple", "orange"])
print(fruit)

# 3

choice = random.choice(["h", "t"])
answer = input("choose between heads and tails h/t \n")
if choice == answer:
    print("you win")
else:
    print("bad luck")
print("computer randomly chose", choice)

# 4
num = random.randint(1, 5)
print(num)
x = int(input("pick a number please : "))
if num == x:
    print("well done")
elif x > 5:
    print("too high")
elif x == 0:
    print("too low")
chance = int(input("pick a second number:  "))
if chance > 5 or chance < 1:
    print("you lose")
else:
    print("you won")

# 5
ran_num = random.randint(1, 10)
print(ran_num)
num = int(input("enter a number :       "))
while ran_num != num:
    num = int(input("enter a number :       "))
    if num == ran_num:
        print("correct")

# 6
score = 0
for i in range(1, 6):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    correct = num1 - num2
    print(num1, '-', num2, '=')
    answer = int(input("enter your answer :    "))
    if answer == correct:
        score += 1
    print("your score is", score)

# 7
clr = random.choice(["green", "red", "orange", "violet", "blue"])
print(clr)
color = input("pick one color:       ")
if clr == color:
    print("well done")
else:
    print("try again you loser")
    color1 = (input("pick a color once again:    "))






