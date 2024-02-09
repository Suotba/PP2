def has_33():
    nums = input("Enter a list: ")
    nums_list = list(map(int, nums.split()))

    for i in range(len(nums_list) - 1):
        if nums_list[i] == 3 and nums_list[i + 1] == 3:
            print("Result:",True)
            return True
    print("Result:",False)
    return False

has_33()
"""
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""