"""წინასწარ განსზაღვრეთ მომხმარებლის უსერის სახელი და პაროლი, მოთხოვეთ ავტორიზაცია,
 წარუმატებლობის შემთხვევაში დაუბეჭდეთ შესაბამისი ტექსტი,
 ავტორიზაციის წარმატებით გავლის შემთხვევაში დაუგენერირეთ 4 ნიშნა რიცხვი და დაუბეჭდეთ. """

import random
username = input("Enter Username: ")
password = input("Enter Password: ")
if username != "Matt" and password != "Muse2000":
    print("Incorrect username or password")
else:
    print("Your UNIQUE code is ",random.randint(1000,9999))