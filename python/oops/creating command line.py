# import argparse

# parser = argparse.ArgumentParser()

# # Add command line arguments
# parser.add_argument("arg1", help="description of argument 1")
# parser.add_argument("arg2", help="description of argument 2")

# # Parse the arguments
# args = parser.parse_args()

# # Use the arguments in your code
# print(args.arg1)
# print(args.arg2)


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--optional", help="description of optional argument", default="default_value")
args = parser.parse_args()
print(args.optional)


# Adding positional arguments
# The following example shows how to add a positional argument to your command line utility:

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("positional", help="description of positional argument")
args = parser.parse_args()
print(args.positional)


import argparse

# Step 1: Create parser
parser = argparse.ArgumentParser(description="Greet someone in different languages")

# Step 2: Add arguments
parser.add_argument('--name', type=str, required=True, help="Enter your name")
parser.add_argument('--lang', type=str, default='english', help="Language (english/hindi)")

# Step 3: Parse arguments
args = parser.parse_args()

# Step 4: Use the arguments
if args.lang.lower() == "english":
    print(f"Hello, {args.name}!")
elif args.lang.lower() == "hindi":
    print(f"Namaste, {args.name}!")
else:
    print(f"Hi {args.name}, language '{args.lang}' not supported.")
