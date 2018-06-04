'''
Given an array of integers, rotate the array by N elements.
Here, N is an integer.

Original Array: [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]

After -1 rotation, => [10, 20, 0, 59, 86, 32, 11, 9, 40, 1]

After 2 rotation => [0, 40, 1, 10, 20, 0, 59, 86, 32, 11]

Hint: Reverse


Here is how the solution works.

Reverse the elements of the original array
Reverse the elements from 0 -> N-1
Reverse the elements from N -> Length-1

'''

# Solution

def reverse_array(arr, start, end):
	while start < end:
		temp = arr[start]
		arr[start] = arr[end]
		arr[end] = temp
		start += 1
		end -= 1

def rotate_array_in_place(arr, rotate):
	length_Arr = len(arr)

	rotate = rotate % length_Arr

	if rotate < 0:
		rotate = rotate + length_Arr

	# Reverse the elements of the original array
	reverse_array(arr, 0, length_Arr - 1)

	# Reverse the elements from 0 -> N-1
	reverse_array(arr, 0, rotate - 1)

	# Reverse the elements from N -> Length-1
	reverse_array(arr, rotate, length_Arr - 1)

	return arr

# Test
print("New array: ", rotate_array_in_place([1, 2, 3, 4,5], 2))

# Runtime: O(n)
# Memory: O(1)