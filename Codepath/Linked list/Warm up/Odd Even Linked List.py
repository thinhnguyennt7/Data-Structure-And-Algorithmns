'''
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...


First make two separate lists, and then join them together with a single pointer assignment.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head


        # Java Solution
		# public class Solution {
		#     public ListNode oddEvenList(ListNode head) {
		#         if (head == null) return null;
		#         ListNode odd = head, even = head.next, evenHead = even;
		#         while (even != null && even.next != null) {
		#             odd.next = even.next;
		#             odd = odd.next;
		#             even.next = odd.next;
		#             even = even.next;
		#         }
		#         odd.next = evenHead;
		#         return head;
		#     }
		# }
		# Time complexity : O(n)
		# Space complexity : O(1)