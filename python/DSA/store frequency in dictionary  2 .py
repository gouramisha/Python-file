text = "amisha"
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Frequencies:", freq)