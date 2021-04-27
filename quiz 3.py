
def  strings(str, str1):
    string = ""
    for char, char1 in zip(str,str1):
        chars = char +char1
        string += chars
    return string

str = input("sheikvanet sitkva :   ")
str1 = input("sheikvanet meore sitkva :   ")
if len(str) == 0 and len(str1) == 0:
    str, str1 = "Hello", "World"
print(strings(str,str1))
