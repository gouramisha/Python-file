# Simple KBC Game for Kids

print("Namaste! KBC game me aapka swagat hai!")

# Humare paas kuch sawal hain
questions = [
    {
        "question": "Bharat ka Rashtriya Pakshi kaun sa hai?",
        "options": ["A. Mor", "B. Kabootar", "C. Kauwa", "D. Hans"],
        "answer": "A"
    },
    {
        "question": "Python programming language kisne banayi?",
        "options": ["A. Guido van Rossum", "B. Bill Gates", "C. Elon Musk", "D. Sundar Pichai"],
        "answer": "A"
    },
    {
        "question": "Duniya ka sabse bada mahadweep kaun sa hai?",
        "options": ["A. Africa", "B. Asia", "C. Europe", "D. Antarctica"],
        "answer": "B"
    }
]

# Hum ek ek karke sawal poochenge
for i in range(len(questions)):
    print("\nSawal", i+1, "hai:")
    print(questions[i]["question"])
    
    # Options dikhate hain
    for option in questions[i]["options"]:
        print(option)
    
    # User se answer lete hain
    answer = input("Apna jawab likho (A, B, C, ya D): ").upper()
    
    # Check karte hain ki jawab sahi hai ya nahi
    if answer == questions[i]["answer"]:
        print("Bahut badhiya!  You earn 10,000 points.")
    else:
        print("Shhhiit!!!!!Apka Jawab galat hai , Maaf kijiye App Sare Points Haar gye.")
        break

print("\nKBC game khelne ke liye dhanyavaad!")
