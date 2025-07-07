with open('poems.txt', 'r') as file:
    content = file.read()

if 'twinkle' in content.lower():
    print("Yes, 'twinkle' is present.")
else:
    print("No, 'twinkle' is not present.")


