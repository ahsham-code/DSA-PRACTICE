#check two list are equal or not

def checkTwoListEqual(list1, list2):
	if(len(list1) != len(list2)):
		return False

	n = len(list1)

	for i in range(0, n):
		if (list1[i] != list2[i]):
			return False

	return True



print (checkTwoListEqual([1,2,2,3], [1, 2,2,3]))
print(checkTwoListEqual([1,2,2,3], [1,2,3,2]))
print(checkTwoListEqual([1,2,2,3], [1,2,2]))

