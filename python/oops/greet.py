import argparse

# Step 1: parser object banao
parser = argparse.ArgumentParser()

# Step 2: argument add karo (positional)
parser.add_argument("name", help="Enter your name")

# Step 3: parse karo command-line arguments
args = parser.parse_args()

# Step 4: output print karo
print(f"Hello, {args.name}!")
