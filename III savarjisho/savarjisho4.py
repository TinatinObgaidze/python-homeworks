"""დაითვალეთ 200 დან 350 მდე კენტი რიცხვების ჯამი.
"""
summ = 0
for number in range(200,350):
    if number % 2 == 1:
        summ += number
print("The sum of the odd numbers is -->", summ)

