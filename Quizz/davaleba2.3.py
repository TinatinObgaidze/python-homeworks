""" მომხმარებელს შეაყვანინეთ რამდენიმე ციფრი, გამოთვალეთ საშუალო არითმეტიკული,
შეადარეთ საშუალო არითმეტიკული პირველ და ბოლო შეყვანილ ციფრს
და დაბეჭდეთ სხვაობა საშუალოსა და ამ ციფრებს შორის"""

numbers = list(map(int,input("enter several numbers:  ").split()))
sashualo = sum(numbers) / len(numbers)
print(sashualo)
round_sashualo = round(sashualo, 2)
dictt = {numbers[0] : "first number", numbers[-1] : "last number", round_sashualo : "sashualo"}
print(dictt)
b = max(dictt)
print(f"am ricxvebs shoris kvealze didia {max(dictt)} -- {dictt.get(b)}")
sxvaoba1 = round_sashualo - numbers[0]
sxvaoba2 = round_sashualo - numbers[-1]
print(" sashualo - first_num =",sxvaoba1,"\n","sashualo - last_num =",sxvaoba2)
