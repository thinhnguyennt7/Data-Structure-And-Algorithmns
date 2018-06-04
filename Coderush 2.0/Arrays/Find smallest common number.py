'''
Given three integer arrays sorted in ascending order, find the smallest number that is common in all three arrays.

For example, let's look at the below three arrays. Here 6 is the smallest number that's common in all the arrays.
1. [6, 7, 10, 25, 30, 63, 64] min = 6

2. [-1, 4, 5, 6, 7, 8, 50] min = 6

3. [1, 6, 10, 14] min = 6


Hint: Three pointer
	Already sorted array to reduce complexity


We should try to think of a way where we can take advantage of the fact that the arrays are sorted in ascending order.

We will use 3 iterators simultaneously to traverse the arrays. We can start off by traversing the arrays from the 0th index,
which will be the smallest value of each array.

If the values of the array indices pointed by the 3 iterators are:

Equal: that's the result. We'll just return the value.
Otherwise, we'll advance the iterator that's pointing to the smallest number among the three.
If any of the iterators has reached the end of the array while we haven't found the common number, we'll return -1

Visualize:
1.

curr_1 at index 0, since it alreay in order sorted acending therefore in first arr 0th is the smallest
[6, 7, 10, 25, 30, 63, 64]

curr_2 at index 0
[-1, 4, 5, 6, 7, 8, 50]

curr_3 at index 0
[1, 6, 10, 14]

2.

[6, 7, 10, 25, 30, 63, 64]

The smallest value in curr_2 is -1 therefore we increament curr_2
[-1, 4, 5, 6, 7, 8, 50]

[1, 6, 10, 14]

3.

[6, 7, 10, 25, 30, 63, 64]

[-1, 4, 5, 6, 7, 8, 50]

The smallest value in curr_3 is 1 therefore we increament curr_3. So it has 6 as minimun now
[1, 6, 10, 14]

4.

[6, 7, 10, 25, 30, 63, 64]

The smallest value in curr_2 is 4 therefore we increament curr_2
[-1, 4, 5, 6, 7, 8, 50]

[1, 6, 10, 14]

5.

[6, 7, 10, 25, 30, 63, 64]

The smallest value in curr_2 is 5 therefore we increament curr_2. So it has 6 as minimun now
[-1, 4, 5, 6, 7, 8, 50]

[1, 6, 10, 14]

6.

curr_1, curr_2, curr_3 are identical. => we return 6.

'''

def find_least_common_number(first, second, third):

	# Initlize the first index for each array
	a = 0
	b = 0
	c = 0

	while a < len(first) and b < len(second) and c < len(third):

		# If the first value in each array already the smallest then return the first value
		if first[a] == second[b] and second[b] == third[c]:
			return first[a]

		if first[a] <= second[b] and first[a] <= third[c]:
			a += 1
		elif second[b] <= first[a] and second[b] <= third[c]:
			b += 1
		elif third[c] <= first[a] and third[c] <= second[b]:
			c += 1
	return -1


# Test
print(find_least_common_number([6, 7, 10, 25, 30, 63, 64], [-1, 4, 5, 6, 7, 8, 50], [1, 6, 10, 14]))

# Time complexoty: O(n)
# Memory: O(1)
