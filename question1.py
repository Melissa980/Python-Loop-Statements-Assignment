# Question 1 Task 1
import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    mood = random.choice(moods)
    print(f"On {day} you were feeling {mood}.")
