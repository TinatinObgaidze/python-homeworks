"""შეიტანეთ ათწილადი რიცხვი, დაამრგვალეთ ათწილად ნაწილში მეათედის სიზუსტით
და დაბეჭდეთ შედეგი. """

def Round(number):
    return round(number,1)
number = float(input("Enter a floating number:\t"))
print(f"Rounded number of {number} is {Round(number)}")