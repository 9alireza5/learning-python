numin = int(input())
genre_list = ["Horror", "Romance", "Comedy", "History", "Adventure", "Action"]
genre_counter = {genre: 0 for genre in genre_list}

for i in range(numin):
    parts = input().split()
    genres = parts[1:]

    for g in genres:
        if g in genre_counter:
            genre_counter[g] += 1

sorted_output = sorted(genre_counter.items(), key=lambda x: (-x[1], x[0]))

for genre, count in sorted_output:
    print(f"{genre} : {count}")
