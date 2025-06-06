# 🔧 Python mein file kaise kholte hain?

# file = open("mera_file.txt", "mode")
# Yahan "mode" ka matlab hai kya karna hai file ke saath:

# 'r' = padhna (read)

# 'w' = likhna (write)

# 'a' = purani file ke aakhir mein kuch aur jodna (append)

# 🖊️ File mein likhna (Write karna)

file = open("mera_file.txt", "w")  # File khol rahe hain write ke liye
file.write("Hello, main tumhari file mein likh raha hoon!\n")
file.write("Ye dusri line hai.")
file.close()  # File band kar do, warna likha hua save nahi hoga
# 📖 File se padhna (Read karna)

file = open("mera_file.txt", "r")  # File read ke liye khol rahe hain
content = file.read()  # Pura content padho
print(content)        # Screen pe dikhao
file.close()
# 💡 Tip: with se file kholna easy hai

with open("mera_file.txt", "r") as file:
    content = file.read()
    print(content)
# with likhne se file khud-b-khud band ho jati hai jab kaam ho jata hai.

# Samjho:
# File ko kholna padta hai pehle

# Fir likhna ya padhna

# Fir file ko band karna zaroori hai