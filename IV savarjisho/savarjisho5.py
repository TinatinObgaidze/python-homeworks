"""დააგენერირეთ 10 შემთხვევითი რიცხვი და დაბეჭდეთ ეკრანზე """
import random
x = 0
for i in range(10):
    x+=1
    print(x,"\t",random.randint(0,1000))

