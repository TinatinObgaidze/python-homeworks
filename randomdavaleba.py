#  1 Write a program that summarizes numbers from 1 to 100:
print(sum(range(100)))

# #  2 Write a program that multiplies numbers from 1 to 100 which is divided by 7:
sia = []
for number in range(0,100,7):
    sia.append(number)
i = 1
for el in sia:
    if el > 0:
        i *= el
print(i)
# an alternative solution:
i = 1
for el in range(1,100):
    if el % 7 == 0:
        i *= el
# print(i)
#
# # 2 same goes here but now  numbers are divided by 11:
for el in range(1,100):
    if el % 11 == 0:
        mult = pow(el,2)
print(mult)
# Now compare the first multiplication with the second:
if i > mult:
    print("first multiplication is greater than second one by",i - mult)
if mult > i:
    print("second multiplication is greater than first one by", mult - i)
 #3 replace all vowels in the text entered by the user with '?':

def no_vowels(text):
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        text = text.replace(vowel,'?')
    return text
text = input("please enter some text here:      ")
print(no_vowels(text))
#
# #4 write a program that uses a random function to get 2 numbers between 1 and 100;
# #calculate the multiplication of numbers placed between these 2 numbers:

import  random
random_sia = []
for i in range(2):
     numbers = (random.randint(1,100))
     random_sia.append(numbers)
     random_sia.sort()
     print(numbers)
print(random_sia)
namravli = 1
for el in range(random_sia[0],random_sia[1]):
    namravli *= el
print(namravli)

# #5 ask user to enter the number; count and print the sum of the digits of the number:

number = int(input("enter the number please :       "))
numbers = str(number)
numbers_sia = list(numbers)
print(numbers_sia)

jami = 0
for i in range(0, len(numbers_sia)):
    numbers_sia[i] = int(numbers_sia[i])
    while jami < len(numbers_sia):
        for el in numbers_sia:
            jami += int(el)
        print(jami)


