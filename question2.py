# Question 2 Task 1
import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times = ["morning", "afternoon", "evening"]

for day in days:
    for time in times: 
      mood = random.choice(moods)
      print(f"On {day} {time} you were feeling {mood}.")