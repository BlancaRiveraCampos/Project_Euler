#Find the 100001st prime #

N = 3
my_list = []
my_list.append(2)

def is_prime(n, a_list):
    for k in a_list:
        if n % k == 0:
            return False
    return True


while len(my_list) < 10001:
    if is_prime(N, my_list):
        my_list.append(N)
        N += 1
    else:
        N += 1

print(my_list[-1])