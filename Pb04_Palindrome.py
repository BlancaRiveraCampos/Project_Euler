#Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome():
    my_list = []
    for n in range(100,1000):
        for a in range(100,1000):
            b = n * a
            b = str(b)
            i = b[::-1]
            if b==i:
                my_list.append(int(b))

    return max(my_list)

print(palindrome())