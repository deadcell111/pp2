def unique(nums):
    unique_set = []
    for num in nums:
        if num not in unique_set:
            unique_set.append(num)
    return unique_set
l = [1,2,3,4,5,2,3,4,5,6]
print(unique(l))