from itertools import permutations
def perm(s):
    pl = [''.join(i) for i in permutations(s)]
    for i in pl:
        print(i)
j = input()
perm(j)