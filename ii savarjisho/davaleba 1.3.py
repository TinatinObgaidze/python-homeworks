"""
დაწერეთ პროგრამა რომელიც მომხმარებელს შეეკითხება მის ხელფასს და თვეში სამუშაო დღეების რაოდენობას,
ამ ინფორმაციაზე დაყრდნობით კი დაუბეჭდავს მის ყოველდღიურ ანაზღაურებას.
"""
salary = int(input("Enter amount of your salary: \n"))
working_days = int(input("Enter number of your working days:\n"))
daily_wage = salary / working_days
print("Your daily wage is -",daily_wage)