"""
Given head nodes of two linked lists that may or may not intersect, find out if they intersect and return the point of intersection; return null otherwise.

Hint: Find length of both linked list, Hash Set

A more efficient solution would be to store nodes of the first linked list in a hashset and then go over the second linked list nodes checking
whether any of the nodes exist in the HashSet. This approach has a linear runtime complexity and linear space complexity.

We can use a much better i.e. O(m + n) linear time complexity algorithm that doesn't require extra memory. To simplify our problem let's
say both the linked lists are of the same size. In this case you can start from heads of both lists, compare their addresses. If these addresses
match means it is an intersection point. If they don't match then move both pointers forward one step and compare their addresses. Repeat this
process until intersection point is found or both of the lists are exhausted. How do we solve this problem if the lists may or may not be of the
same length? We can extend the linear time solution with one extra scan of linked lists to find their lengths. Below is the complete algorithm.

	Find lengths of both linked lists: L1 and L2
	Calculate difference in length of both linked lists: d = |L1 - L2|
	Move head pointer of longer list 'd' steps forward
	Now traverse both lists, comparing nodes until we find a match or reach the end of lists

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def get_length(self, head):
        list_length = 0
        while head != None:
            head = head.next
            list_length += 1
        return list_length

    def getIntersectionNode(self, headA, headB):
        list1Node = None
        list1Length = self.get_length(headA) # Get the first list length
        list2Node = None
        list2Length = self.get_length(headB) # Get the second list length

        length_Diff = 0

        # In case the length of first list is greater or equal to length of second list
        if list1Length >= list2Length:
            length_Diff = list1Length - list2Length
            list1Node = headA
            list2Node = headB

        # Otherwise
        else:
            length_Diff = list2Length - list1Length
            list1Node = headB
            list2Node = headA

        # In case if the length is greater than 0 then find the list1Node
        while length_Diff > 0:
            list1Node = list1Node.next
            length_Diff -= 1

        while list1Node != None:
            if list1Node == list2Node:
                return list1Node

            list1Node = list1Node.next
            list2Node = list2Node.next
        return None

# Time: O(m+n)
# Memory: O(1)