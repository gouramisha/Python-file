# import	Kisi aur code ko yaha laata hai taaki use use kar sakein
import math

print(math.sqrt(16))  # Output: 4.0


import random

print("🎲 Welcome to the Lucky Number Game!")
print("I am thinking of a number between 1 and 10.")

secret_number = random.randint(1, 10)  # 1 se 10 ke beech random number banega

guess = int(input("Your guess: "))  # User se number puchho

if guess == secret_number:
    print("🎉 Hurray! You guessed it right!")
else:
    print(f"😞 Oops! The correct number was {secret_number}")
