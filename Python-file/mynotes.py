with open("my_notes.txt", "w") as file:
    file.write("Apples are red.\n")
    file.write("Bananas are yellow.\n")
    file.write("Grapes are green.\n")

with open("my_notes.txt", "r") as file:
    data = file.read()
    print("READ():")
    print(data)

with open("my_notes.txt", "r") as file:
    print("READLINE():")
    print(file.readline())
    print(file.readline())
    print(file.readline())


with open("my_notes.txt", "r") as file:
    lines = file.readlines()
    print("READLINES():")
    print(lines)

with open("my_notes.txt", "r") as file:
    for line in file.readlines():
        fruit, color = line.strip().split(" are ")
        print(f"Fruit: {fruit}, Color: {color}")