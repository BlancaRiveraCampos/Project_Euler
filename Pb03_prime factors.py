#Find the largest prime factor of the # 600851475143

def is_prime(n):
    for k in range(2,n):
        if n % k == 0 and k != n:
            return False
        else:
            return True


def find_fac(N):
    fac = 1
    fact_list = []
    while N > 1:
        if N % fac == 0:
            if is_prime(fac):
                N = N/fac
                fact_list.append(fac)
            else:
                fac += 1
        else:
            fac += 1
    return fact_list

print(find_fac(600851475143))