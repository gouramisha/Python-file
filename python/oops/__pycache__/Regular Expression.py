import re

text = "My phone number is 9876543210"
pattern = r"\d{10}"

match = re.search(pattern, text)
if match:
    print("Found:", match.group())


# | Pattern | Meaning                                |
# | ------- | -------------------------------------- |
# | `.`     | Any character except newline           |
# | `\d`    | Any digit (0–9)                        |
# | `\D`    | Any non-digit                          |
# | `\w`    | Any word character (a-z, A-Z, 0–9, \_) |
# | `\W`    | Any non-word character                 |
# | `\s`    | Space                                  |
# | `^`     | Start of string                        |
# | `$`     | End of string                          |
# | `*`     | 0 or more                              |
# | `+`     | 1 or more                              |
# | `?`     | 0 or 1                                 |
# | `{n}`   | Exactly n times                        |
# | `{n,m}` | Between n and m times                  |
