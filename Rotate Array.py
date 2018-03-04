# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1 or len(nums) == 0 or k == 0:
            return             

        k = k % len(nums)
        self.reverse(nums,0,len(nums) - 1)
        self.reverse(nums,0,k - 1)
        self.reverse(nums,k,len(nums) - 1)

    def reverse(self, nums, start, end):
        i = start
        j = end
        while j > i and i < len(nums):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

