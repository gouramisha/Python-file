# file = open("example.txt", "r")
# content = file.read()          # pura file ek string mein read karega
# print(content)
# file.close()

# for line in open("example.txt", "r"):
#     print(line.strip())


file = open("example.txt", "w")
file.write("Hello World!\n")
file.write("This is a test file.\n")
file.close()

# File ko append mode mein kholna
file = open("example.txt", "a")

# Naya content add karna
file.write("Yeh nayi line hai jo append hui hai.\n")

# File band karna
file.close()