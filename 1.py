c = input("Enter your string:")
li = c.split(" ")
for w in li:
    print(w[-1: :-1])