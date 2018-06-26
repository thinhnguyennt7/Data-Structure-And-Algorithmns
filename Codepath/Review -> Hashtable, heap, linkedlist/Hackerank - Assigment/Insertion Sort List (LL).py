
'''
Sort a linked list using insertion sort

1. Insertion sort iterates, cosuming one input element each repetition, and growing a sorted output list
2. At each iteration, iteration sort removes one element from the input data, finds the location it belongs within the sorted list and inserted in there
3. It repeats until no input elements remains.

Example 1:
inout: 4 -> 2 -> 1 -> 3
Outout: 1 -> 2 -> 3 -> 4
'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Helper function to insert node
def sorted_insertHP(head, node):
    if node == None:
        return head
    if head == None or node.val <= head.val:
        node.next = head
        return node
    curr = head
    while curr.next != None and curr.next.val < node.val:
        curr = curr.next
    node.next = curr.next
    curr.next = node
    return head

#  Main function
def insertionSortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    sortedLL = None
    curr = head

    while curr != None:
        temp = curr.next
        sortedLL = sorted_insertHP(sortedLL, curr)
        curr = temp
    return sortedLL