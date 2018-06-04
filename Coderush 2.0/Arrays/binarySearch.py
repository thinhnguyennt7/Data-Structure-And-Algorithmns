'''
BINARY SEARCH

Hint: Divide and conquer

Here's how algorithm works:
	1. At every step, consider the array between low and high indices
	2. Calculate the mid index.
	3. If element at the mid index is the key, return mid.
	4. If element at mid is greater than the key, then reduce the array size such that high becomes mid - 1. Index
		at low remains the same.
	5. If element at mid is less than the key, then reduce the array size such that low becomes mid + 1. Index
		at high remains the same.
	6. When low is greater than high, key doesn't exist. Return -1

	[1, 10, 20 , 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]

	Looking for index of number 47.
	low = value(1), index = 0
	high = value(222), index = 19
	mid = value(107), index = 9
	key = 47

	mid = 107 > key => move to the left 1. -> high = index(mid)-1
	mid = index(4), value(59)


	mid = 59 > key => move to the left 1. -> high = index(mid)-1,
	mid = index(1), value(10)


	mid = 10 < key => low move to index 2, mid will be at index 2
	low = value(20) index(2)
	mid = value(20) index(2)

	mid = 20 < key => low move to index 3, mid will be at index 3
	low = value(47) index(3)
	mid = value(47) index(3)

	mid = 47 == key
	return mid

'''

# Given a sorted array of integers, return the index of the given key. Return -1 if not found.
# [1, 10, 20 , 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]

def binary_search(a, key):
	return binary_search_recursive(a, key, 0, len(a) - 1)

def binary_search_recursive(a, key, low, high):
	if low > high:
		return -1

	mid = low + ((high - low) // 2)
	if a[mid] == key:
		return mid
	elif key < a[mid]:
		return binary_search_recursive(a, key, low, mid - 1)
	else:
		return binary_search_recursive(a, key, mid + 1, high)

print("Recursive: ", binary_search([1, 10, 20 , 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222], 47))

# Runtime : O(logn)
# Memory: O(logn)
# Recursive solution has O(logn) memory complexity as it will consume memory on the stack.


# Second way to solve it
# [1, 10, 20, 47, 59, 63, 75, 88]
# low = value(1), index(0)
# high = value(88), index(end)
# mid = value(59), index(4)
# key = 70

#	mid = 59 < key => low = index(mid) + 1
#	low = value(63)
#	mid = value(75), index(6)
#	high = value(88), index(end)


#	mid = 75 > key, index(6), high move to index 5, => high = value(63)
#	mid = index(5), value(63)
#	low = value(63)

#	mid = 63, high move to index 4, => high = value(59)
#	high < low => return -1

def binary_search_iterative(a, key):
	low = 0
	high = len(a) - 1
	while low <= high:
		mid = low + ((high + low) // 2)
		if a[mid] == key:
			return mid
		elif a[mid] > key:
			high = mid - 1
		else:
			low = mid + 1
	return -1

print("Iterattive: ", binary_search_iterative([1, 10, 20, 47, 59, 63, 75, 88], 47))

# Runtime : O(logn)
# Memory: O(1)