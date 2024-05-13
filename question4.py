# Question 4 Task 1
import random

options = ["Rock", "Paper", "Scissors"]

user_guess = input("Guess which option your opponent selected (Rock, Paper, Scissors): ")

selected_option = random.choice(options)
print(f"Here is my choice: {selected_option}.")

if user_guess == selected_option:
    print("You guessed my choice, well done!")
else:
    print("Sorry, you did not guess correctly.")
