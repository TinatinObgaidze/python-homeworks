"""დაბეჭდეთ ფიბონაჩის რიცხვები რომლებიც  0 -დან  77 მდეა. """
def fibbo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibbo(n -1) + fibbo(n -2)
for n in range(100):
    if fibbo(n) > 77:
        break
    print(n,"-->", fibbo(n))



