#Find the difference between the sum of the squares of the first 100 natural # and the square of the sum.

my_list = []

def sum_squares():
    for x in range(1,101):
        y = x**2
        my_list.append(y)
    z = sum(my_list)
    a = (sum(range(1,101)))**2
    return a - z

print(sum_squares())