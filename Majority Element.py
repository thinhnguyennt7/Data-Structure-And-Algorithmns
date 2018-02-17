# Given an array of size n, find the majority element. The majority element
# is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always
# exist in the array.


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
                
        for j in dict.keys():
            if dict[j] == max(dict.values()):
                return j
            
            
          
# class Solution:
#     def majorityElement(self, nums):
#         counts = collections.Counter(nums)
#         return max(counts.keys(), key=counts.get)