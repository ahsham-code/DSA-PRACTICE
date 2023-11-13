#Recursion function
#Non Recursion function

# Recursion Function

# f(x) = f(x - 1) + f(x - 2)  -> f(x) is recursive function
# f(x) = g(x) + 2 -> f(x) is not a recursive function


''' f(0) = 1, f(1) = 1 #base case ya terminal case
# f(x) = f(x-1) + f(x-2) for x >= 2 # recursive case
# f(5) = ?
# f(5) = f(4) + f(3)
	   = f(3) + f(2) + f(2) + f(1)
	   = f(2) + f(1) + f(1) + f(0) + f(1) + f(0) + f(1)
	   = f(1) + f(0) + 1+ 1+ 1 + 1+ 1 + 1
	   = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
	   = 8


1, 1, 2, 3, 5,8, 13, 21, 34,.... [fibbonacci series] '''


def f(x):
	if x < 2:
		return 1
	else:
		return f(x-1) + f(x-2)

print (f(5))


