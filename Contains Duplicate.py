# Given an array of integers, find if the array contains any duplicates. Your function should
# return true if any value appears at least twice in the array, and it should return false
# if every element is distinct.

# Using hashmap
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        for j in dict.values():
            if j > 1:
                return True

        return False
