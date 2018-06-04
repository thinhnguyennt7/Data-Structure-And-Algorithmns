'''
Search a given number in a sorted array that has been rotated by some arbitrary number. Return -1 if the number does not exist.

Original Array: [1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]

After performing rotation on this array 6 times it changed:
				[176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162]


Hint: Linear search is not acceptable solution must be done in binary search

Complexity: runtime: O(Log n)

The solution is essentially binary search with some modifications. If we look at the array in example closely, we notice that at
least one half of the array is always sorted. We can use this property to our advantage. If the number n lies within the sorted half
of the array then our problem is basic binary search. Otherwise discard the sorted half and keep examining the unsorted part. Since we
are partitioning array in half at each step this gives us O(logn) runtime complexity.

Visualize: [176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162]
	looking key = 200
1. 	low = index(0), value(176)
	high = index(19), value(162)
	mid = index(9), value(47)

	Since the second half of the array is sorted and 200 is not part of it's range (59 - 162) we will continue our search on the first half

2. 	low = index(0), value(176)
	high = index(8), value(20)
	mid = index(4), value(200)

	Since the first half of the array is sorted and 200 is part of it's range (176 - 210) we will continue our search on the first half

3.	low = index(0), value(176)
	high = index(3), vlaue(200)
	mid = index(1), value(188)

	Since 200 is greater than mid index (188) we continue our second on second half

4.	low = index(2), value(199)
	high = index(3), value(200)
	mid = index(2), value(199)

	Sicne 200 is greater than mid index (199), we continue our search on second half

5.	low = index(3), value(200)
	high = index(3), value(200)
	mid = index(3), value(200)

	Key is found at index 3 and return 3.
'''

# Solution
def binarySearch(arr, low, high, key):
	if low > high:
		return -1

	mid = low + (high - low)//2

	if arr[mid] == key:
		return mid

	if (arr[low] < arr[mid] and key < arr[mid] and key >= arr[low]):
		return binarySearch(arr, low, mid - 1, key)

	elif (arr[mid] < arr[high] and key > arr[mid] and key <= arr[high]):
		return binarySearch(arr, mid + 1, high, key)

	elif arr[low] > arr[mid]:
		return binarySearch(arr, low, mid - 1, key)

	elif arr[high] < arr[mid]:
		return binarySearch(arr, mid + 1, high, key)

	return -1

def searchRotatedArray(arr, key):
	return binarySearch(arr, 0, len(arr)-1, key)

# Test

print(searchRotatedArray([176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162], 200))

# Complexity: runtime: O(Log n)