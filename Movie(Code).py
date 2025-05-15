
## favorite movie #1           #2       #3          #4             #5             #6         #7      38
favorite_movies = ["batman", "flash", "openhimer", "walking dead","Blade Runner","gary man","breaking bad","The Matrix"]
release_years = [1999,     1972,     2024,        1994,        1994,     2018    ,       2001 , 1999]
                 #1         #2        #3           #4           #5          #6               #7   #8  
# Get the favorite movie name from the user
favorite_movie = input(f"Enter your favorite movie between: \n{favorite_movies}\n:")

# Check for common years
common_years = []
for i in range(len(favorite_movies)):
    if favorite_movie == favorite_movies[i]:
        for j in range(i+1, len(favorite_movies)):
            if release_years[i] == release_years[j]:
                common_years.append(release_years[i])

if len(common_years) == 0:
    print("There is no film in list ")
else:
    print("Shared movie is:")
    for i in range(len(favorite_movies)):
        if favorite_movie == favorite_movies[i]:
            for j in range(i+1, len(favorite_movies)):
                if release_years[i] == release_years[j]:
                   print(favorite_movie, "and", favorite_movies[j], "year",[release_years[i]],"is share movies")
