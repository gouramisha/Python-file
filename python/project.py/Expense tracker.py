import os

# File to store data
filename = "data.txt"

# Function to add transaction
def add_transaction():
    type = input("Enter type (income/expense): ").lower()
    category = input("Enter category (food, rent, travel, etc.): ").capitalize()
    amount = float(input("Enter amount: ₹ "))
    
    with open(filename, "a") as file:
        file.write(f"{type},{category},{amount}\n")
    print("✅ Transaction added successfully!\n")

# Function to show summary
def show_summary():
    income = 0
    expense = 0
    categories = {}

    if not os.path.exists(filename):
        print("No data found.\n")
        return

    with open(filename, "r") as file:
        for line in file:
            type, category, amount = line.strip().split(",")
            amount = float(amount)

            if type == "income":
                income += amount
            elif type == "expense":
                expense += amount
                categories[category] = categories.get(category, 0) + amount

    print(f"\n💰 Total Income: ₹{income}")
    print(f"💸 Total Expense: ₹{expense}")
    print(f"📊 Balance: ₹{income - expense}\n")

    if categories:
        print("📂 Expense by Category:")
        for cat, amt in categories.items():
            print(f"  - {cat}: ₹{amt}")
    print()

# Main menu
def main():
    while True:
        print("📘 Personal Expense Tracker")
        print("1. Add Transaction")
        print("2. Show Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, try again!\n")

# Run the program
main()
