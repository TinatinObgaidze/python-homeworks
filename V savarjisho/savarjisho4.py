def capitalization(string):
    if string[0].isupper():
        return("yay")
    else:
        return (string.capitalize())
string = input("Text here:\t")
print(capitalization(string))

text = input("text here:\t")
sia = list(text.split(" "))
for i in sia:
    if i.isupper():
        print("yay")
    else:
        print(i.capitalize())
