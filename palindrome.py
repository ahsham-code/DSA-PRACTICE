def is_pal(l,N,i):
	if i>=N//2:
		return True
	else:
		return (l[i]==l[N-1-i]) and is_pal(l,N,i+1)

print(is_pal([1,2,2,1],4,0))
print(is_pal([1,2,2,1,2],5,0))
print(is_pal([1,2,2,2,2,1],6,0))
print(is_pal([1,1,2,2,1,1],6,0))

print(is_pal([1,2,1],3,0))