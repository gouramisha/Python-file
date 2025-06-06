filename = input("Emter file name:")
lines = []
print("Enter content and press any time \"exit \" to write")
while True:
    line =  input()
    if line == 'exit':
        break
    else:
      lines.append(line)
print(lines)