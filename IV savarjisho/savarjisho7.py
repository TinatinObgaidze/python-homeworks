"""მომხმარებელს მოთხოვეთ შეიყვანოს საწყისი და საბოლოო რიცხვები, და შეიყვანოს რიცხვი რომლის ჯერადების ნამრავლიც გვაინტერესებს.
 გადაამოწმეთ რომ სამივე შეყვანილი სიმბოლო  არის რიცხვი, გამოვთვალოთ საწყისი რიცხვიდან საბოლოო რიცხვამდე იმ რიცხვების ნამრავლი
 რომელიც არის მესამე შეყვანილი რიცხვის ჯერადი."""

first_num = int(input("First num:   "))
last_num =int(input("Last num:    "))
multiples_of_num= int(input("multiples of number :   "))
product= 1
for numbers in range(first_num, last_num):
    if numbers % multiples_of_num == 0:
        product = product * numbers
print(f"The product of numbers from {first_num} to {last_num} that is multiple of {multiples_of_num} is : ",product)
