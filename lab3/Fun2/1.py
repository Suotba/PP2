def is_above_5_5(movie):
    if movie["imdb"] > 5.5:
        return True

name = input("Movie name: ")
imdb = float(input("IMDB score: "))
category = input("Category: ")

movie_info = {
    "name": name,
    "imdb": imdb,
    "category": category
}

result = is_above_5_5(movie_info)
print(result)
