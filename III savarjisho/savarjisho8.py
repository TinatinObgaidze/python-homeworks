"""მომხმარებელს სთხოვეთ შეიყვანოს ორი რიცხვი და დაბეჭდეთ ამ ორ რიცხვს შორის მოთავსებული რიცხვების ჯამი.
თუ მომხმაარებელმა შეყვანის დროს დაუშვა შეცდომა, თავიდან მოთხოვეთ ინფორმაციის შეყვანა მანამ,
სანამ სწორად არ შეიყვანს"""
number1 = input("enter integers:\t")
number2 = input("enter integers:\t")
while not number1.isdigit() and not number2.isdigit():
    print("sorry, you should enter ONLY integers")
    number1 = input("enter integer:\t")
    number2 = input("enter integer:\t")
sum = 0
for i in range(int(number1), int(number2)):
    sum+=i
print("The sum is",sum)