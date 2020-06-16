#Find the sum of the even numbers in the Fibonacci sequence between 1 and 4M.

fib_list = [1, 2]

def fib(list_f, i):
	x = 0
	y = 2
	while x < i:
		x = list_f[-1] + list_f[-2]
		if x % 2 == 0:
			y = y + x
		list_f.append(x)

	return y

print(fib(fib_list,4000000))
