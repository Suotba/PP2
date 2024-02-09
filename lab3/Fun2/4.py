def avg_IMDB(movie):
    count_a = 0
    count_b = 0

    if movie["imdb"] > 0:
        count_a += movie["imdb"]
        count_b += 1

    

    avg = count_a / count_b
    return avg

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

    


result = avg_IMDB(movie)
print("Average IMBD:",result)
