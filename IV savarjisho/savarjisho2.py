"""შეიტანეთ სამი რიცხვი, იპოვეთ მათ შორის მინიმუმი და დაბეჭდეთ შედეგი.
 გამოიყენეთ min  ფუნქცია."""
def Minimal(num1,num2,num3):
    return min(num1,num2,num3)
num1 = float(input("Enter num:\t"))
num2 = float(input("Enter num:\t"))
num3 = float(input("Enter num:\t"))
print(Minimal(num1,num2,num3))
