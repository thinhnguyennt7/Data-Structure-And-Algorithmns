def insertionSort(arr):
	for j in range(1,len(arr)):
		key = arr[j]
		i = j - 1
		while i >= 0 and arr[i] > key:
			arr[i+1] = arr[i]
			i -=1
		arr[i+1] = key
	return arr


print(insertionSort([5,2,4,6,1,3]))


# Steps:
# [5,2,4,6,1,3]
# [2,5,4,6,1,3]
# [2,4,5,6,1,3]
# [2,4,5,6,1,3]
# [1,2,4,5,6,3]
# [1,2,3,4,5,6]