'''
Given an array (list) of intervals as input where each interval has
a start and end timestamps.
You are required to merge overlapping intervals and return output array
(list).

Consider below input array. Intervals (1, 5), (3, 7), (4, 6), (6, 8)
are overlapping so should be merged to one big interval (1, 8).
Similarly intervals (10, 12) and (11, 15) are also overlapping intervals
and should be merged to (10, 15).

Hint: Linear Scan


Here is the approach we are following.

List of input intervals is given, and we'll keep merged intervals in output
list
For each interval in the input list
if input interval is overlapping with the last interval in output
list then we'll merge these two intervals and update last interval of
output list with merged interval
otherwise, we'll add input interval to the output list.

'''

# IF IT NO SORT YET
def find_interval(intervals):

	# Check if there is no interval
	if len(intervals) == 0:
		return None

	# Sort the interval
	intervals.sort() # O(nlogn)

	curr = intervals[0]
	merged = []

	for i in range(1,len(intervals)):

		if overlap(curr, intervals[i]):
			curr = combieInter(curr, intervals[i])

		else:
			merged.append(curr)
			curr = intervals[i]

	merged.append(curr)
	return merged

# Check if the two intervals are overlap or not
def overlap(interval1, interval2):
	return interval1[1] >= interval2[0]

# Combie the two interval when overlapping
def combieInter(interval1, interval2):
	return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

# print("Merge Overlap interval: ", find_interval([[1,5], [3,7], [4,6], [6,8], [10, 12], [11, 15]]))
print("Merge Overlap interval that hasn't sort: ", find_interval([[1,5], [3,7], [4,6], [6,8], [11, 15], [10, 12]]))
# Expected answer: [[1,8],[10,15]]
# Time Complexity: O(nlogn)
# Memory: O(n)

###################################################################################################################


# IF IT SORTED ALREADY
def find_interval(intervals):

	# Check if there is no interval
	if len(intervals) == 0:
		return None

	curr = intervals[0]
	merged = []

	for i in range(1,len(intervals)):

		if overlap(curr, intervals[i]):
			curr = combieInter(curr, intervals[i])

		else:
			merged.append(curr)
			curr = intervals[i]

	merged.append(curr)
	return merged

# Check if the two intervals are overlap or not
def overlap(interval1, interval2):
	return interval1[1] >= interval2[0]

# Combie the two interval when overlapping
def combieInter(interval1, interval2):
	return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

print("Merge Overlap interval that has sorted: ", find_interval([[1,5], [3,7], [4,6], [6,8], [10, 12], [11, 15]]))
# Expected answer: [[1,8],[10,15]]
# Time Complexity: O(n)
# Memory: O(n)