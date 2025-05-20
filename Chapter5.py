# CHAPTER 5 – DICTIONARY & SETS   
# Dictionary is a collection of keys-value pairs.
a = {
"key": "value",
"harry": "code",
"marks": "100",
"list": [1, 2, 9]
}
print(a["key"])   # Output: "value"
print(a["list"])  # Output: [1, 2, 9]

# Dict 
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}

print(car["model"])   # Output kya hoga

# Sets
# Set is a collection of non-repetitive elements.
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.
# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
# Hindi to English dictionary
hindi_english_dict = {
    "पुस्तक": "book",
    "सेब": "apple",
    "कुत्ता": "dog",
    "बिल्ली": "cat",
    "पानी": "water",
    "खिड़की": "window",
    "दरवाज़ा": "door",
    "आकाश": "sky",
    "पेड़": "tree",
    "घर": "house"
}

print("हिंदी-इंग्लिश शब्दकोश (Hindi-English Dictionary)")
print("आप किसी भी हिंदी शब्द का अंग्रेज़ी अनुवाद जान सकते हैं।\n")

while True:
    word = input("हिंदी शब्द दर्ज करें (या 'exit' लिखें बंद करने के लिए): ")

    if word == "exit":
        print("धन्यवाद! शब्दकोश बंद हो गया।")
        break

    translation = hindi_english_dict.get(word)
    if translation:
        print(f"अंग्रेज़ी अनुवाद: {translation}\n")
    else:
        print("माफ़ कीजिए, यह शब्द शब्दकोश में नहीं है।\n")


# Write a program to input eight numbers from the user and display all the unique numbers (once).

