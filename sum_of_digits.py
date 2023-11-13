def sum(N):
	if N==0:
		return 0
	else:
		return (N%10 + sum(N//10))
print(sum(1234))
print(sum(1))