def numeric(string):
    str = ""
    for i in string:
        if i.isdigit():
            str += i
    return str
string = input("text here:\t")
print(numeric(string))
