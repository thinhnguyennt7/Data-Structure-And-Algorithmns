"""
Given the head of a singly linked list and 'N', swap the head with Nth node. Return the head of the new linked list.

Original linked list: 7 -> 14 -> 21 -> 28 -> 35 -> 42 -> Null
N = 4

After swaping: 28 -> 14 -> 21 -> 7 -> 35 -> 42 -> Null

Hint: Find (N-1)th node
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def swap_Head_with_Nth(self, head, n):

		prev = None
		current = head

		# Default check if head is none and n not greater than 1
		if head == None or n == 1:
			return head

		count = 1
		while current != None and count < n:
			prev = current # Prev is N-1
			current = current.next
			count += 1

		if current == None:
			return head

		# Current is pointing to nth node
		# Let's swap nth node with head
		prev.next = head
		temp = head.next
		head.next = current.next
		current.next = temp

		return current
# Time: O(n)
# Memory: O(1)