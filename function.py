def sum(a, b):
	return a + b

def diff(a, b):
	return a - b

def mult(a, b):
	return a * b

def div(a, b):
	return a/b

def calculator(a, b, c):
	if c == '+':
		return sum(a, b)

	if c == '-':
		return diff(a, b)

	if c == '*':
		return mult(a, b)

	if c == '/':
		return div(a, b)

	else :
		print("Unknown sign")

print(sum(calculator(5, 4, '+'),calculator(5, 6, '+')))
print(calculator(5, 4, '*'))
print(calculator(5, 4, '-'))
print(calculator(5, 4, '/'))
print(calculator(5, 4, '$'))
