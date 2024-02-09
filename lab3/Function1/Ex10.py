def unique(nums):
    un = []
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            un.append(nums[i])
    un.append(nums[-1])  
    return un

nums = input("Enter a list: ")
nums_list = list(map(int, nums.split()))

nums_list.sort()

result = unique(nums_list)
print("Unique elements:", result)
