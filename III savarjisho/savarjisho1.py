"""შეიყვანთ 2 რიცხვი. ციკლის გამოყენებით დაბეჭდეთ შეყვანილი რიცხვების საერთო გამყოფები. """


number1 = int(input("Enter the number:\t"))
number2 = int(input("Enter the number:\t"))
x = 0
while x < number2:
    x+=1
    if number2 % x == 0 and number1 % x == 0:
        print(f"The common divisor of {number1} and {number2} is -->",x)