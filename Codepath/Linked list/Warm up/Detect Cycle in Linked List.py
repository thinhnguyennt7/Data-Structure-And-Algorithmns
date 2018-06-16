'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Complexity O(N) Space O(1)
        # Two Pointers technique
        if head == None or head.next == None:
            return False
        slow = head
        fast = slow.next
        while fast and fast.next:
            if fast == slow or fast.next == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False

    # Complexity O(N) Space O(N)
    # Using Set
    def hasCycle(self, head):
    	curr = head
    	aux = set()
    	while curr.next != None:
    		if curr in aux:
    			return True
			aux.add(curr)
			curr = curr.next
		return False

# "List 5 --> 7 --> None"
# False
# "List 5 --> 7 --> 5"
# True