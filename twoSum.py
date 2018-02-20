# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


#With out hash table, complexity O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        for i, j in enumerate(nums): 
            reminder = target - j
            # Make value at index become empty 
            nums[i] = []
            if reminder in nums:
                    return [i, nums.index(reminder)]


# With hashtable, complexity O(n)
class Solution(object):
    def twoSum(self, nums, target):
        
        # Create a hash table
        hash = {}
        for i, value in enumerate(nums): 
            reminder = target - value
            if reminder in hash:
                return hash[reminder], i
            hash[value] = i
                


# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].