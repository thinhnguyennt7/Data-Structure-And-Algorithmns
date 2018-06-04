"""
Given two sorted linked lists, merge them such that the resulting linked list is also sorted.

Give list 1: 4 -> 8 -> 15 -> 19 -> Null
Given list 2: 7 -> 9 -> 10 -> 16 -> Null

After merge: 4 -> 7 -> 8 -> 9 -> 10 -> 15 -> 16 -> 19 -> Null

Hint: Use two iterators to scan both lists

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def mergeTwoSorted(self, head1, head2):
        if head1 == None:
            return head2
        elif head2 == None:
            return head1

        mergedHead = None

        if head1.val <= head2.val:
            mergedHead = head1
            head1 = head1.next
        else:
            mergedHead = head2
            head2 = head2.next

        mergedTail = mergedHead

        while head1 != None and head2 != None:
            temp = None
            if head1.val <= head2.val:
                temp = head1
                head1 = head1.next
            else:
                temp = head2
                head2 = head2.next

        mergedTail.next = temp
        mergedTail = temp

        if head1 != None:
            mergedTail.next = head1
        elif head2 != None:
            mergedTail.next = head2

        return mergedHead
# Time: O(m+n)
# Memory: O(1)