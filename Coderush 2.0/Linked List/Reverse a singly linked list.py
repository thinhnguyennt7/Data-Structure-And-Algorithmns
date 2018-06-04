"""
Given the pointer/reference to the head of a singly linked list, reverse it and return the pointer/reference to the head of reversed linked list.

Consider the following linked list.
head -> 7 -> 14 -> 21 -> 28 -> NULL

Return pointer to the reversed linked list as shown in the figure.
head -> 28 -> 21 -> 14 -> 7 -> NULL


# Iterative way
If linked list only contains 0 or 1 nodes, then the current list can be returned as it is. If there are two or more nodes,
then iterative solution starts with 2 pointers.

reversed: A pointer to already reversed linked list (initialized to head).
list_to_do: A pointer to the remaining list (initialized to head->next).
We then set the reversed->next to NULL. This becomes the last node in the reversed linked list. reversed will always point to the head
of the newly reversed linked list.

At each iteration, the list_to_do pointer moves forward (until it reaches NULL). The current node becomes the head of the new reversed linked
list and starts pointing to the previous head of the reversed linked list.

The loop terminates when list_to_do becomes NULL and reversed pointer is pointing to the new head at the termination of the loop.


# Recursive way
First thing to remember (and to mention to the interviewer as well) is that the recursive version uses stack. OS allocates stack memory and this solution
can run out of memory for really large linked lists (think billions of items).

We recursively visit each node in the linked list until we reach the last node. This last node will become the new head of this list. On the return path,
each node is going to append itself to the end of partially reverse linked list.

Here's how recursive reversal works. If you have a reversed linked list of all the nodes to the left of current node and you know the last node of the reversed
inked list, then inserting the current node as the next of the last node will create the new reversed linked list. Then return the head of the new linked list.
The trick here is that you don't explicitly need to track the last node. The next pointer in the current node is already pointing to the last node
in the partially reversed linked list. Confused? An example might help. Here's our favorite linked list at the start when recursive reverse function is called.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

	# Iterative
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        todo = head.next
        reverse = head
        reverse.next = None

        while (todo != None):
            temp = todo
            todo = todo.next
            temp.next = reverse
            reverse = temp
        return reverse
        # Time: O(n)
        # Memory: O(1)


    # Recursive
    def reverseList(self, head):
    	if head == None or head.next == None:
            return head

        reverse = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reverse
        # Time: O(n)
        # Memory: O(n)
