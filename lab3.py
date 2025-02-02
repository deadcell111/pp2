l = [1, 2, 3, 4, 5]
def filter_prime(x):
    if x > 1:
        for i in range (2, (x//2) + 1):
            if x % i == 0:
                return False
        return True
for i in range(len(l)):
    if(filter_prime(l[i])):
        print(l[i])