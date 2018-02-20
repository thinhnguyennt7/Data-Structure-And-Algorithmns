
# Given a sorted array, remove the duplicates in-place such that each element 
# appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying 
# the input array in-place with O(1) extra memory.

# Example:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of 
# nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.



class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        # Create two pointers
        j = 1
        i = 0
        while (j < len(nums)):
            if nums[i] == nums[j]:
                j = j + 1
            else:
                i = i + 1
                nums[i] = nums[j]
                j += 1

        # Return the value
        return i + 1
        