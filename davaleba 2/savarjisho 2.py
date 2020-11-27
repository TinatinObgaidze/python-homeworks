# user should guess the secret number and he only have 3 attempts
secret_number = 10
guess_underline_count = 0
guess_limit = 3
while guess_underline_count < guess_limit:
    guess = int(input('Guess:  '))
    guess_underline_count += 1
    if guess == secret_number:
        print("you win!")
        break
else:
    print('Sorry, you failed!')
