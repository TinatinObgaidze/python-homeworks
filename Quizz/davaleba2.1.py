""" პროგრამის მომხმარებელს მოთხოვეთ შეიყვანოს მცირე ტექსტი, ამ ტექსტში მოძებნეთ სიტყვა “Beautiful”,
თუ სიტყვა არის მოცემულ ტექსტში,
მომხმარებელს დაუბრუნეთ რაიმე პასუხი, თუ ვერ მოიძებნა, მომხმარებელს დაუწერეთ რომ არასწორად აკეთებს რაღაცას.
"""

text =  input("sheikvanet raime text:\t")
if "beautiful"  in text:
    print(f"textshi 'beautiful' napovnia {text.count('beautiful')} jer")
else:
    print("samwuxarod text-shi ver moidzebna sitkva beautiful")