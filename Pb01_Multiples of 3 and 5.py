#Find the sum of the multiples of 3 or 5 below 1000.
my_list = []

def divisible(n):
    for n in range(1,n):
        if n % 15 == 0:
            my_list.append(n)
            n += 1
        elif n % 3 == 0 or n % 5 == 0:
            my_list.append(n)
            n += 1
        else:
            n += 1
    return sum(my_list)

print(divisible(1000))