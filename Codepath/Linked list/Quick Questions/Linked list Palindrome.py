'''
Given a singly linked list, determine if it is a palindrome. Could you do it in O(n) time and O(1) space?

Input: 1->2->2->1
Output: true
'''
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	# Time: O(N), Space O(N)
	def isPalindrome(self, head):
		arr = []
		while head:
			arr.append(head.val)
			head = head.next
		return arr == arr[::-1]

	def isPalindrome(self, head):
		fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True

