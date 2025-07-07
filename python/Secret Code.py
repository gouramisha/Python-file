# Secret symbol dictionary for each letter
secret_dict = {
    "A": "@", "B": "#", "C": "$", "D": "%", "E": "&",
    "F": "*", "G": "!", "H": "~", "I": "?", "J": "^",
    "K": ">", "L": "<", "M": "=", "N": "+", "O": "|",
    "P": "}", "Q": "{", "R": "]", "S": "[", "T": ":",
    "U": ";", "V": ",", "W": ".", "X": "/", "Y": "(", "Z": ")"
}

# Function to encode message
def bana_secret(text):
    secret = ""
    for ch in text.upper():  # convert to uppercase
        if ch in secret_dict:
            secret += secret_dict[ch]
        else:
            secret += ch  # keep space or number same
    return secret

# Encode "HELLO"
message = (input("Type any word"))
secret_message = bana_secret(message)

print("Normal Message:", message)
print("Secret Message:", secret_message)
