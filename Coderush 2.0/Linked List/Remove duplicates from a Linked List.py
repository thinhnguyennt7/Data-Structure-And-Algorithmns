"""
We are given a linked list of integers and we have to remove all the duplicate nodes from it by keeping only
the first occurrence of each duplicate.

The following example elaborates it further.

Original: 7 -> 14 -> 28 -> 14 -> 21
Result: 7 -> 14 -> 28 -> 21

Hint: Use hashset

"""

# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printList(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def removeDuplicates(self):
        if self.head == None:
            return self.head

        dup_set = set()
        dup_set.add(self.head.val)
        curr = self.head

        while curr.next != None:

            if curr.next.val in dup_set:
                curr.next = curr.next.next

            else:
                dup_set.add(curr.next.val)
                curr = curr.next

        return self.head.val

    # Time: O(n)
    # Memory: O(n)

# Driver
l = LinkedList()
l.insert(7)
l.insert(14)
l.insert(28)
l.insert(14)
l.insert(21)
l.printList()
print("########")
print("After remove duplicated:")
l.removeDuplicates()
l.printList()
