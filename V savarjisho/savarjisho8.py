nums = "12345678900234845738"
string = list(nums)
for i in string:
    while len(string) > 4:
        del string[3]
        print(string)
        if len(string) ==4:
            break
