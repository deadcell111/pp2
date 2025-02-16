def first(n):
    cnt = 1
    while cnt <= n:
        yield (cnt**2)
        cnt += 1
n = int(input())
ftr = first(n)
"""for n in ctr:
    print(n)"""
    
def second(n):
    for i in range(0,n + 1):
        s = str(i)
        if i % 2 == 0:
            if i >= 0 and i != n:
                yield(s) + ','
            else:
                yield(s)
setr = second(n)
"""for n in setr:
    print(n, end = " ")"""

def third(n):
    for i in range(0,n):
        if i % 3 == 0 and i % 4 == 0:
            yield(i)
tr = third(n)
for n in tr:
    print(n)

def squared(a,b):
    for i in range(a,b + 1):
        yield(i **2)
a = int(input())
b = int(input())
frd = squared(a,b)
for n in frd:
    print(n, end = " ")


def fifth(n):
    while n >= 0:
        yield(n)
        n -= 1
n = int(input())
fif = fifth(n)
for i in fif:
    print(i, end = " ")