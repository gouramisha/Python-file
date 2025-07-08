def word_counter(text):
    # Remove punctuation and convert to lowercase
    for ch in ".,!?;:":
        text = text.replace(ch, "")
    text = text.lower()

    words = text.split()  # split by spaces
    total_words = len(words)

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return total_words, freq

# Option 1: Get text from user input
text = input("Enter a paragraph:\n")

# Option 2: Or read from a file
# with open('sample.txt', 'r') as file:
#     text = file.read()

total, frequencies = word_counter(text)

print("\nTotal Words:", total)
print("\nWord Frequencies:")
for word, count in frequencies.items():
    print(f"{word}: {count}")
