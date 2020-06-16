#Find the smallest positive # evenly divisible by all the # between 1 and 20

a = 1
b = 20

def divisible(x,n):
    for i in range(1,n+1):
        if x % i != 0:
            return False
    return True

while not divisible(a, b):
    a += 1

print(a)