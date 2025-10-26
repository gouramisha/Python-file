import random

# Options
options = ["Rock", "Paper", "Scissors"]

# AI Players
def ai_player1():
    # Random choice
    return random.choice(options)

def ai_player2():
    # Random choice or you can add a simple pattern AI
    return random.choice(options)

# Decide winner
def decide_winner(choice1, choice2):
    if choice1 == choice2:
        return "Draw"
    elif (choice1 == "Rock" and choice2 == "Scissors") or \
         (choice1 == "Paper" and choice2 == "Rock") or \
         (choice1 == "Scissors" and choice2 == "Paper"):
        return "AI Player 1 wins!"
    else:
        return "AI Player 2 wins!"

# Main game
rounds = 5
for i in range(rounds):
    c1 = ai_player1()
    c2 = ai_player2()
    print(f"Round {i+1}: AI Player 1 chooses {c1}, AI Player 2 chooses {c2} => {decide_winner(c1, c2)}")
