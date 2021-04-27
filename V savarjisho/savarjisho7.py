array = []
strings = input("text here:\t")
for i in strings:
    if i.isdigit():
        array.append(i)
print(max(array))

