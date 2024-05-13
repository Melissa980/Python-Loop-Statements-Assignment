# Question 6 Task 1
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

selected_genres = genres[1:4]  

for genre in selected_genres:
    print(genre)


# Question 6 Task 2
genres_with_music = [genre + ' Music' for genre in genres]

print(genres_with_music)


# Question 6 Task 3
count = 10

while count >= 1:
    print(count)
    count -= 1
    
print("The beat drops now!")

