text =" My name is Amisha Gour"
filename = "abc.txt"
#write
file = open(filename,"w")
print(type(file))
#print(type(file))
file.write(text)

file.close()

print("Write done")