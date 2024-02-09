def show_histogram():
    n = input("Enter a list: ")
    n_list = list(map(int, n.split()))
    for i in n_list:
        print("*" * i)

show_histogram()
