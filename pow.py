def pow(a,b):
	if (b==0):
		return 1
	else:
		return (a*pow(a,b-1))
print(pow(2,3))
print(pow(2,0))
print(pow(0,2))