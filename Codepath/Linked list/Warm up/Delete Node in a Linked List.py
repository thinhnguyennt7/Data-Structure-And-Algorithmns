'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

    4 -> 5 -> 1 -> 9
Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list
             should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list
             should become 4 -> 5 -> 9 after calling your function.
Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.

There is no way to delete the current node without a reference to the parent;
think about solutions that allow a logical deletions without a literal deletion.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        #   node.val equals 3
        #   node.next.val equals 4
        #   node.val assigned the value of 4
        # Output
        #   1 -> 2 -> 4 -> 4

        node.next = node.next.next
        # node.next = third node
        # node.next.next = NULL/None
        # node.next assigned NULL/None
        # Output
        #   1 -> 2 -> 4


    # Time and space complexity are both O(1)O(1).


    # Leetcode: 237. Delete Node in a Linked List