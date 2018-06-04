"""
Given a singly linked list, return nth node from last. Return null if 'n' is out-of-bounds.

Hint: Move two pointers which are n nodes apart.

We will use two pointers to find the nth from the last node. The idea is to have two pointers n nodes apart:
	one pointing to the head and the other pointing to the nth node. Then we move both pointers forward until
	the second pointer reaches the tail. Now the first pointer will be pointing to the nth node from last.
	And if we reach the tail before making both pointers n nodes apart, that means n is out of bounds.


"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def find_nth_from_last(self, head, n):
		if head == None or n < 1:
			return None

		# We use two pointers head and tail , where head and tail are 'n' nodes apart
		tail = head

		# Move the tail to the nth node
		while tail != None and n > 0:
			tail = tail.next
			n -= 1

		# Check if out of bound
		if n != 0:
			return None

		# When tail pointer reaches the end of the list, then head is pointing at nth node.
		while tail != None:
			tail = tail.next
			head = head.next
		return head

# Time: O(n)
# Memory: O(1)