def spy_game():
    nums = input("Enter a list: ")
    nums_list = list(map(int, nums.split()))
    
    for i in range(len(nums_list) - 1):
        if nums_list[i] == 0 and nums_list[i + 1] == 0 and nums_list[i + 2] == 7 :
            print("Result: ",True)
            return True
    print("Result: ",False)
    return False

spy_game()
