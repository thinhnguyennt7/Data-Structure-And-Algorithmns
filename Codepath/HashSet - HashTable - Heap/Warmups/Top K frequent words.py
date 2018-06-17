'''
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same
frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
	Note that "i" comes before "love" due to a lower alphabetical order.


Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
	with the number of occurrence being 4, 3, 2 and 1 respectively.


Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

'''
import heapq

def top_k_frequent(words, k):
	word_to_count = calculate_count(words) # {word: count}
	#[(count, word), (count2, word2), .....] Tuple
	word_count_pairs = []
	for word, count in word_to_count.items():
		word_count_pairs.append((-count, word)) # The reason to put the negative here
		# because in the default of heapq, it do the min heap instead the maxheap

	heapq.heapify(word_count_pairs) # transform word_count_pair into heap
	result = []
	for i in range(k):
		result.append(heapq.heappop(word_count_pairs)[1]) # heappop the smallest item off the heap since we are in min heap
														# The [1] is because we only want the word not the number
	return result

# Helper method that calculate the number of time words appear in the list
def calculate_count(words):
	diction = {}
	for word in words:
		if word in diction:
			diction[word] += 1
		else:
			diction[word] = 1
	return diction


input = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print("Solution:", top_k_frequent(input, k))

# Time: Time Complexity: O(N log k), where N is the length of words.
# We count the frequency of each word in O(N) time, then we add N words to
# the heap, each in O(logk) time. Finally, we pop from the heap up
# to k times. As k ≤ N, this is O(Nlogk) in total.

# In Python, we improve this to O(N+klogN): our heapq.heapify
# operation and counting operations are O(N), and each of k heapq.heappop
# operations are O(logN).

print("#######")
print("Time: O(N + K logN")

print("Space: O(N)")

