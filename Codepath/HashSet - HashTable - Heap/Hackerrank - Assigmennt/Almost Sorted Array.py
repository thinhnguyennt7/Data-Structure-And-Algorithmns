'''
Given an almost sorted array, in which each number is less than m spots array from its correctly sorted position, and
the value m, write an algorithmn that will return an array with the element properly sorted.

An example input would be the list [3, 2, 1, 4, 6, 5] and m = 3. In the example, each element in the array is less than 3
spots array from its position in a sorted array.
The snippet below is a buggy solution to the problem above. Fix the buggy solution such that it solves the problem
'''

def sort_list(almost_sorted_list, m):
    min_heap, result = [], []
    for elem in almost_sorted_list[:m]:
        heapq.heappush(min_heap, elem)

    for elem in almost_sorted_list:
        heapq.heappush(min_heap, elem)
        result.append(heapq.heappop(min_heap))

    for i in range(len(min_heap)):
        result.append(heapq.heappop(min_heap))

    output = []
    for i in result:
        if i not in output:
            output.append(i)
    return output