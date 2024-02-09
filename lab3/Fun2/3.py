def cat(movie_list):
    return [movie for movie in movie_list if movie["category"] == cat_need]

cat_need = input("Which category you are looking for: ")
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

filtered_movies = cat(movies_info)
print("Your movies: ")
print(filtered_movies)
