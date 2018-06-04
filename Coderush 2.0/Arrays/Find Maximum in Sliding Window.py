'''
Given a large array of integers and a window of size w, find current maximum in the window as the window slides
through the entire array.

Consider the array below and let's try to find all maxiumin with window size = 3
[-4, 2, -5, 3, 6]

Step 1: For the first 3 elements in windows, max is 2
	max = 2 [-4, 2, -5, 3, 6]
Step2: Slide window one position to the right, and max now for the window become 3
	max = 3 [-4, 2, -5, 3, 6]
Step3: In the last windows, max is 6
	max = 6 [-4, 2, -5, 3, 6]

With this type of problem is helpful if we use:
	Heap,
	Double singular linked list

Runtime: Linear O(n)
Memory: O(W), w is the windows size

A simple solution to this problem would be to find maximun by scanning all elements within the window w everythime it slides right. But the complexity now is
	O(NW)

A slightly better solution will be to use Heap of window size w. It will help us find the max quickly. One thing to note is that every time the window moves;
we will need to delete one of the existing elements from the heap that is not in the window anymore, and we will need to add a new element.
Both of these operations are O(log w) operations. The total runtime complexity for this approach will be O(n log w). Let's challenge ourselves
to see if we can come up with a better runtime.

We can reduce the complexity of the previous solution by using a doubly linked list (or a vector) where we can insert/delete at both ends.
Notice that at Step 2 in the above example, when we get the newest element 3 in the window it is greater than all existing elements in the
window (2, -5) and, in this case, the elements 2 and -5 can be safely removed from the data structure holding the window. This property is critical
for achieving a linear time solution of the problem. Here is the basic algorithm we will use to get a better runtime.

Window size is w and array size is n
Iterate the first w elements of array; and for each element in the array, do the following:
remove elements from the tail of window (list) that are smaller than or equal to the current element
push current element at the tail of window
The above step will ensure that the maximum of first w elements is at the head of linked list and it can be printed
Run through remaining elements of the array and for each element do the following:
remove all elements from the tail of window that are smaller than or equal to the current element
remove the element at head if its index no longer falls in current window
push the current element at the tail of window
current max is at head and can be printed


Solution visualation:
array: [-4, 2, -5, 1, -1, 6]
window: []

1. First iteration: Add -4 to the linked list
window: [-4]
2. Second iteration: -4 is removed from the linked list as it;s less than 2 and we add 2 at the tail of linked list. Which is a head
window: [2]
3. Thir iteration: -5 is added to the tail of linked list after 2. since -5 < 2. At this point we are done with the first w elements and their maximun is at head is 2
window: [2, -5]


4. Sliding window one step right, we see element 1 which is greater than -5 at the tail of linked list so it is removed and we add it to the tail.
window: [2, 1]
5. Sliding window another step right we see element -1 adn we add it to the tail of linked list. Also since 2 has fallen out of current windes we evict 2 from
the head of linked list . Max now is 1
window: [1, -1]
6. Sliding window another step right we see 6 and it removed all elements lesser than itself in the linked list and become the max.
window: [6]

'''
# Solution

import collections

def findMax_sliding_window(arr, windowSize):
	result = []

	# Check if the window size larger than the length of entire arr then return nothing
	if windowSize > len(arr):
		return

	window = collections.deque()

	# Find out the max of the first windows
	for i in range(0, windowSize): # Know the specific stopping therefore it O(1)
		while window and arr[i] >= arr[window[-1]]:
			window.pop()
		window.append(i)

	#  Max of the first windows
	result.append(arr[window[0]])

	#  Sliding the window to the right
	for i in range(windowSize, len(arr)):

		# Remove all the numbers that are smaller than current number
		# from the tail of list
		while window and arr[i] >= arr[window[-1]]:
			window.pop()

		# Remove first number if it doesn't fall in the window anymore
		if window and (window[0] <= i - windowSize):
			window.popleft()
		window.append(i)
		result.append(arr[window[0]])

	print(result)

# Test
findMax_sliding_window([-4, 2, -5, 1, -1, 6], 3)
# Output: [2, 2, 1, 6]

# Similar problem in leetcode: 239. Sliding Window Maximum


# Runtime: Linear O(n)
# Memory: O(W), w is the windows size