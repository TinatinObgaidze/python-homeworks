# 1
name = str(input("please enter your name:\n"))
print(len(name))

# 2
name = str(input("what's your name ? \t"))
surname = str(input("what's your surname? \t"))
print(len(name + surname))

# 3
name = str(input("enter your name in lower case:     "))
surname = str(input("enter your surname in lower case:    "))
name = name.title()
surname = surname.title()
print(name + " ", surname)

# 4
phrase = str(input("daweret mesaflavis pirveli xazi :   "))
length = (len(phrase))
print('This has', length, "letters in it")

# 5
word = str(input("enter any word:   "))
word = word.upper()
print(word)

# 6
name = input("enter your first name :  ")
if len(name) > 5:
    surname_1 = input("enter your surname:  ")
    name = name + surname_1
    print(name.upper())
else:
    print(name.lower())








