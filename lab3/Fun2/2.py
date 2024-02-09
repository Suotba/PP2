def filter_movies_above_5_5(movie_list):
    return [movie for movie in movie_list if movie["imdb"] > 5.5]


movies_info = []
while True:
    name = input("Movie name: ")
    
    if name.lower() == 'all':
        break
    
    imdb = float(input("IMDB score: "))
    category = input("Category: ")

    movie = {
        "name": name,
        "imdb": imdb,
        "category": category
    }

    movies_info.append(movie)

filtered_movies = filter_movies_above_5_5(movies_info)
print("IMDB score above 5.5:")
print(filtered_movies)
