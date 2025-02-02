from itertools import permutations
def unique(nums):
    unique_set = []
    for num in nums:
        if num not in unique_set:
            unique_set.append(num)
    return unique_set
def perm(s):
    pl = [''.join(i) for i in permutations(s)]
    for i in pl:
        print(i)
l = [1,2,3,4,5,1,2]
print(unique(l))
u= "asd"
print(perm(u))