'''
Given an integer array, sort it in ascending order using quicksort.

Original array: [55, 23, 26, 2, 25]
Sorted array: [2, 23, 25, 26, 55]

Hint: divide and conque
	  Hoare's algorithm

Here is an overview of how the quicksort algorithm works.
	Select a pivot element from the array. We can pick the first element as the pivot (following Hoare's algorithm).
	Another common approach is to select a random element as the pivot.
	Reorder the array by comparing with the pivot element such that smaller values end up at the left side, and the larger
	values end up at the right side of the pivot.
	Now, the pivot element is in its correct sorted position.
	Applying the above steps, we can recursively sort the sublists on the right and left sides of the pivot.


arr[] = {10, 80, 30, 90, 40, 50, 70}
Indexes:  0   1   2   3   4   5   6

low = 0, high =  6, pivot = arr[h] = 70
Initialize index of smaller element, i = -1

Traverse elements from j = low to high-1
j = 0 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 0
arr[] = {10, 80, 30, 90, 40, 50, 70} // No change as i and j
                                     // are same

j = 1 : Since arr[j] > pivot, do nothing
// No change in i and arr[]

j = 2 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 1
arr[] = {10, 30, 80, 90, 40, 50, 70} // We swap 80 and 30

j = 3 : Since arr[j] > pivot, do nothing
// No change in i and arr[]

j = 4 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 2
arr[] = {10, 30, 40, 90, 80, 50, 70} // 80 and 40 Swapped
j = 5 : Since arr[j] <= pivot, do i++ and swap arr[i] with arr[j]
i = 3
arr[] = {10, 30, 40, 50, 80, 90, 70} // 90 and 50 Swapped

We come out of loop because j is now equal to high-1.
Finally we place pivot at correct position by swapping
arr[i+1] and arr[high] (or pivot)
arr[] = {10, 30, 40, 50, 70, 90, 80} // 80 and 70 Swapped

Now 70 is at its correct place. All elements smaller than
70 are before it and all elements greater than 70 are after
it.

'''

# Solution
def quickSort(arr, low, high):
	if low < high:

		# Pi is the partitioning index, arr[p] is now at right place
		pi = partition(arr, low, high)

		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)
	return arr


def partition(arr, low, high):
	i = low - 1
	pivot = arr[high]

	for j in range(low, high):

		# If the current element is less than or equal to pivot
		if arr[j] <= pivot:
			i += 1 # Increment i
			arr[i], arr[j] = arr[j], arr[i] # Swapping value

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i + 1

array = [10, 80, 30, 90, 40, 50, 70]
length = len(array)
print("Sorted Array:", quickSort(array, 0, length-1));

# Time: Worst case: O(n^2), Average case: O(nlogn)
# Memory: O(log n)