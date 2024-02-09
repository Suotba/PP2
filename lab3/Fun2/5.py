def avg_IMDB(movie_list, look_cat):
    count_a = 0
    count_b = 0

    for movie in movie_list:
        if movie["imdb"] > 0 and movie["category"] == look_cat:
            count_a += movie["imdb"]
            count_b += 1

    avg = count_a / count_b if count_b > 0 else 0
    return avg

movie_list = []
look_cat = input("Which category: ")

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

    movie_list.append(movie)

result = avg_IMDB(movie_list, look_cat)
print("Average IMDB:", result)

