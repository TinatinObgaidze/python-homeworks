def STR(string):
    if len(string) > 5:
        return string[0] + string[-2:]
string = input("Enter some str here:\t")
print(STR(string))