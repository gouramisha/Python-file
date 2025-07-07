# with open("my_notes.txt", "r") as f:
#     print(f.tell())     # 🔹 Yeh batayega: file ki ungli shuru mein kahan hai (0)
#     f.read(5)           # 🔹 Pehle 5 letters padho: "Hello"
#     print(f.tell())     # 🔹 Ab pointer 5 par chala gaya hai

# Seek #tell
# with open("demo.txt", "w") as f:
#  with open("demo.txt", "r") as f:
#     print("Start at:", f.tell())   # 0
#     f.read(10)
#     print("After reading 10:", f.tell())  # 10
#     f.seek(5)
#     print("After seek to 5:", f.tell())   # 5
    # print("Reading again:", f.read(5))    # 5 se 5 chars padhega


# with open("my_notes.txt", "r") as f:
#     f.seek(0)         # 🧠 Start pe jaao
#     print(f.read(5))  # Output: Hello
    
#     f.seek(5)         # 🧠 Ab 6th letter se padho
#     print(f.read(5))  # Output: World

with open("demo.txt", "r") as f:
    f.seek(0)         # 🧠 Start pe jaao
    print(f.read(5))  # Output: Hello
    
    f.seek(5)         # 🧠 Ab 6th letter se padho
    print(f.read(5))  # Output: World