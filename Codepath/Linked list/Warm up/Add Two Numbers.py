'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


Think about how we can map the math operations to operations on linked list.

Enumerate the boundary conditions carefully.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers_Linked_list(self, list1, list2):

        # Initlize
        carryOut = 0
        finalList = root = ListNode(0)

        while list1 or list2 or carryOut:

            value1 = value2 = 0

            # Get val of list 1
            if list1:
                value1 = list1.val
                list1 = list1.next

            # Get val of list 1
            if list2:
                value2 = list2.val
                list2 = list2.next

            carryOut, actualVal = divmod(value1 + value2 + carryOut, 10)

            root.next = ListNode(actualVal)
            root = root.next

        return finalList.next # Has to be .next otherwise it will inclue 0 in font.