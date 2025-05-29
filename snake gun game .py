import random  # Random choice banane ke liye

# Options
choices = ['s', 'w', 'g']  # s = Snake, w = Water, g = Gun

# User ka input
user = input("Choose (s for Snake, w for Water, g for Gun): ")

# Computer ka random choice
computer = random.choice(choices)

# Dono choices print kar do
print("You chose:", user)
print("Computer chose:", computer)

# Winner decide karo
if user == computer:
    print("It's a Draw!")

elif user == 's' and computer == 'w':
    print("You Win! 🐍 drinks 💧")

elif user == 'w' and computer == 'g':
    print("You Win! 💧 drowns 🔫")

elif user == 'g' and computer == 's':
    print("You Win! 🔫 kills 🐍")

else:
    print("You Lose!")
