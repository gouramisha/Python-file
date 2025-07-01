def game():
    return 85  # Example score; replace with real logic

score = game()

try:
    with open('Hi-score.txt', 'r') as f:
        hi_score = f.read()
        hi_score = int(hi_score) if hi_score else 0
except FileNotFoundError:
    hi_score = 0

if score > hi_score:
    with open('Hi-score.txt', 'w') as f:
        f.write(str(score))
    print("New high score:", score)
else:
    print("No new high score.")
