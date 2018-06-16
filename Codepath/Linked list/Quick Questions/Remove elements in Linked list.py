'''
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6

Return: 1 --> 2 --> 3 --> 4 --> 5
'''
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeElement(self, val):
		if head == None:
			return head
		prev = head
		curr = head.next
		while curr!= None:
			if curr.val == val:
				if curr == head:
					head = head.next
					curr = head
				else:
					prev.next = curr.next
					curr = curr.next
			else:
				prev = curr
				curr = curr.next
		return head
