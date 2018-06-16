"""
Given head of a linked list and a key, delete node with this given key from the linked list.

Hint: Keep track of previous pointer.
"""

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

    # Delete the node at the specific key (Dummy head technique, Two pointers)
    def deleteNode(self, key):
        # Check edge case
        if self.head == None:
            return self.head

        # Algorithmns
        prev = None
        current = self.head
        while (current != None):
            if current.val == key:
                if current == self.head:
                    head = self.head.next
                    current = self.head
                else:
                    prev.next = current.next
                    current = current.next
            else:
                prev = current
                current = current.next

        return self.head

    # Time: O(N)
    # Memory: O(1)

# Driver
l = LinkedList()
l.insert(7)
l.insert(14)
l.insert(28)
l.insert(14)
l.insert(21)
l.printList()
print("########")
print("After remove:")
l.deleteNode(7)
l.printList()