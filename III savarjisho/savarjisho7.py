"""	მომხამარებელს დააბეჭდინეთ ტექსტი, და დათვალეთ რამდენჯერ შეგვხვდა ასო ‘ე’ ამ ტექსტში."""
text = input("Enter some text:\t")
for char in text:
    if char == "e":
        number= text.count(char)
print(f"we found {number} 'e' in the text")

