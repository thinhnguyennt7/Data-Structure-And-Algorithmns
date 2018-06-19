'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution:
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		ln = len(nums)
		if ln < 4:
			return []

		nums.sort()
		ans = set()
		for i in range(ln-3):

			if i>0 and nums[i-1]==nums[i]:
				continue

			ctarget1 = target - nums[i]
			for j in range(i+1,ln-2):
				if j > i+1 and nums[j-1]==nums[j]:
						continue
				t = {}
				for k in range(j+1,ln):
						ctarget2 = ctarget1-nums[j]-nums[k]
						if nums[k] in t:
							elem = (nums[i],nums[j],ctarget2,nums[k])
							ans.add(elem)
						else:
							t[ctarget2] = 1

		return sorted(list(ans))