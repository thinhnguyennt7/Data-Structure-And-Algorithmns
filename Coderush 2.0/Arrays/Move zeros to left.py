'''
Given an integer array, move all elements containing '0' to the left while maintaining the order of other elements in the array.

Let's look at the following integer array.
[1, 10, 20, 0, 59, 63, 0, 88, 0]

After moving all zero elements to the left, the array should look like this. We need to maintain the order of non-zero elements.
[0, 0, 0, 1, 10, 20, 59, 63, 88]

Hint:
	Counting
	Reader/Writer

We will keep two markers (read_index and write_index) and point them to the end of the array. Here is an overview of the algorithm.

1
	While moving read_index towards the start of the array:
2
	if read_index points to '0', skip
3
	if read_index points to non-zero, write to write_index and decrement write_index

Visualize:
Original Array: [1, 10, 20, 0, 59, 63, 0, 88, 0]

1. Starting at the last index of the array. Two pointers at that index is read and write
2. If arr[read] = 0, then write will stay here, and we decrement read to another cell.
3. If arr[read] != 0 then we need to update write index. We need to decrement both write and read
4. If arr[read] again = 0 then no need to update array. Write will not change, we'll decrement read.
5. If arr[read] != 0 then we need to update write index. We need to decrement both write and read

[1, 10, 20, 0, 59, 63, 0, 88, 0]
[1, 10, 20, 0, 59, 63, 0, 88, 88]
[1, 10, 20, 0, 59, 63, 0, 63, 88]
[1, 10, 20, 0, 59, 63, 59, 63, 88]
[1, 10, 20, 0, 59, 20, 59, 63, 88]
[1, 10, 20, 0, 10, 20, 59, 63, 88]
[1, 10, 20, 1, 10, 20, 59, 63, 88]
[1, 10, 0, 1, 10, 20, 59, 63, 88]
[1, 0, 0, 1, 10, 20, 59, 63, 88]
[0 0, 0, 1, 10, 20, 59, 63, 88]
'''

# Solution
def move_zeros_to_left(arr):
	if len(arr) < 1:
		return

	write_index = len(arr) - 1
	read_index = len(arr) - 1

	while read_index >= 0:
		if arr[read_index] != 0:
			arr[write_index] = arr[read_index]
			write_index -= 1

		read_index -= 1

	while write_index >= 0:
		arr[write_index] = 0
		write_index -= 1

	return arr

# Test
print(move_zeros_to_left([1, 10, 20, 0, 59, 63, 0, 88, 0]))

# Output: [0 0, 0, 1, 10, 20, 59, 63, 88]

# Time: O(n)
# Memory: O(1)