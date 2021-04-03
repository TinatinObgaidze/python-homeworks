import random
words = ["rock","paper","scissors"]
you = 0
computer = 0
time = 0
while time < 3:
    your_choice = input("Please enter your choice (rock/paper/scissors):\n ")
    words_generator = random.choice(words)
    print(words_generator)
    time +=1

    if your_choice == "rock" and words_generator == "paper":
        computer+=1
    elif your_choice == "paper" and words_generator == "rock":
        you+=1
    elif your_choice == "paper" and words_generator == "scissors":
        computer+=1
    elif your_choice == "scissors" and words_generator == "rock":
        you+=1
    elif your_choice == "rock" and words_generator == "scissors":
        you +=1
    elif your_choice == "scissors" and words_generator == "rock":
        computer+=1
    elif your_choice == words_generator:
        you += 0
        computer += 0
    elif time == 3:
        break

print(f"you : {you}     vs     computer : {computer}")
if you > computer:
    print("You won!")
elif you == computer:
    print("Draw")
else:
    print("You lost")