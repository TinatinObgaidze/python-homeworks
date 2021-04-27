def STR(string):
    return string + string[-2 :] * 3
string = input("Enter some str here:   ")
print(STR(string))