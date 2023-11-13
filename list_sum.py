def f(l,n,i):
	if i>=n:
		return 0
	else:
		return (l[i]+f(l,n,i+1))
print(f([2,4,3,2],4,1))
print(f([2,4,3,2],4,2))
print(f([2,4,3,2],4,3))
print(f([2,4,3,2],4,4))
print(f([2,4,3,2],4,5))
print(f([2,4,3,2],4,7))
print(f([2,4,3,2],4,8))