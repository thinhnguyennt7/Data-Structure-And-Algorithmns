'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.


Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

import collections
import heapq

def frequencySort(s):
	res=""
	dic=collections.defaultdict(int)
	for i in s:
		dic[i]+=1

	heap=[ (dic[i],i) for i in dic ]
	print("heap: ", heap)
	heapq.heapify(heap) # Min heap
	while heap:
			i,j=heapq.heappop(heap)
			res=j*i+res
			print("res: ", res)
	return res

# Driver test
if __name__ == "__main__":
	# input = "tree"
	input = "cccaaa"
	print("Solution: ", frequencySort(input))