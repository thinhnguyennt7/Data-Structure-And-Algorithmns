'''
Given a sorted array of integers, return the low and high index of the given key. Return -1 if not found.
The array length can be in millions with lots of duplicates.

Original array: [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]

In the following example, low and high indices would be:

Key: 1, Low=0 and High=0

Key: 2, Low=1 and High=1

Key: 5, Low=2 and High=9

key: 20, Low=10 and High=10


HINT: BINARY SEARCH


Algorithm for finding the low index.

1
	At every step, consider the array between low and high indices
2
	Calculate the mid index.
3
	If element at mid index is less than the key, low becomes mid + 1 (to move towards start of range)
4
	If element at mid is greater or equal to the key, high becomes mid - 1. Index at low remains the same.
5
	When low is greater than high, low would be pointing to the first occurrence of the key.
6
	If element at low does not match the key, return -1.


Let's find low and high indices of 5 in the given example below:
Original array: [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]

'''
# Solution

def findLowIndex(arr, key):
	low = 0
	high = len(arr) - 1
	mid = high // 2

	# Binary Search for low index
	while low <= high:

		if arr[mid] < key:
			low = mid + 1
		else:
			high = mid - 1

		mid = low + (high - low)//2

	if arr[low] == key:
		return low

	return -1


def findHighIndex(arr, key):
	low = 0
	high = len(arr) - 1
	mid = high // 2

	# Binary Search for high index
	while low <= high:

		if arr[mid] <= key:
			low = mid + 1
		else:
			high = mid - 1

		mid = low + (high - low)//2

	if arr[high] == key:
		return high

	return -1


print("Low index: ", findLowIndex([1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20], 5))
print("High index: ", findHighIndex([1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20], 5))

# Time: O(log n)
# Memory: O(1)