#    Hashing -  Prestoring values into same data structure

s = "hello"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

