# Question 5 Task 1
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for track_number, genre in enumerate(genres, 1):
    print(f"Track {track_number}: {genre} - Enjoy your {genre} music!")


# Question 5 Task 2
track_number = 1

while track_number <= len(genres):
    genre = genres[track_number - 1]  
    print(f"Track {track_number}: {genre} - Enjoy your {genre} music!")
    
    if genre == 'Hip-hop':
        print("Stopping the loop because Hip-hop was played.")
        break
    
    track_number += 1


# Question 5 Task 3
for track_number in range(len(genres)):
    genre = genres[track_number]  
    
    if genre != 'Classical':
        print(f"Track {track_number + 1}: Light show ready for {genre} music.")
    else:
        print(f"Track {track_number + 1}: Skipping light show for {genre} music.")