'''
Given a linked list, remove the n-th node from the end of list and return its head.
Note that the given n will always be valid.

Example:

Given 1->2->3->4->5, and n = 2.

Return 1->2->3->5

'''

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def Palindrome(self, head):
		"""
		:type head: ListNode
		:rtype: void Do not return anything, modify head in-place instead.
		"""