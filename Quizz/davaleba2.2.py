"""" მომხმარებლის მიერ შეყვანილ ტექსტში მოძებნეთ სიტყვები, “small”, “Tall”, “middle”,
თუ ტექსტში აღმოჩნდება რომელიმე მათგანი, დაწერეთ პირველივე სიტყვა რაც აღმოჩნდა და დაასრულეთ პროგრამა
თუ ტექსტში აღმოჩნდება რომელიმე მათგანი, დაწერეთ პირველივე სიტყვა რაც აღმოჩნდა და დაასრულეთ პროგრამა.
დაუბეჭდეთ ყველა სიტყვა რომელიც კი იპოვეთ.
თუ ვერც ერთი სიტყვა აღმოაჩინეთ მაშინ დაუბეჭდეთ რომ რაღაცას არასწორად აკეთებს.
"""

words = ["small", "Tall", "middle"]
text = input("sheikvanet  mcire text:\t")
text_array = list(text.split(" "))
for i in text_array:
    if i in words:
        print("Pirvelive napovni sitkva aris --",i)
        break
words_list = []
for i in text.split(" "):
    if i in words:
        words_list.append(i)
words_dict= {
    "small" : words_list.count("small"),
    "Tall" : words_list.count("Tall"),
    "middle" : words_list.count("middle")
}

print("sul vipovet: ",words_dict)
if text_array  not in  words:
        print("sworad sheikvanet sitkvebi")

