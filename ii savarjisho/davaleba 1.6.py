""" შექმენით კალკულატორი, რომელიც გაშვებისას გვკითხავს პირველ მნიშნელობას,
შემდეგ მეორე მნიშვნელობას და შემდეგ მათემატიკურ ოპერატორს. პასუხი დაგვიბრუნოს ტერმინალში
"""
num1 = int(input("number :"))
num2 = int(input("number :"))
operator = input("operator :")
calculator = "{}{}{}".format(num1,operator,num2)
print(eval(calculator))

