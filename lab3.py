l = []
a = int(input("add size of list: "))
for i in range(a):
    b = int(input())
    l.append(b)
isp = lambda x: x > 1 and all(x % i != 0 for i in range(2,(x // 2)+1))
primes = list(filter(isp,l))
print("Prime numbers from list: ")
for i in primes:
    print(i)