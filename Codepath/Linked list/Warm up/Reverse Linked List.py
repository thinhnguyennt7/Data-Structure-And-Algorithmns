'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


hink about which pointers need to be updated, and which of their values need to be temporarily stored.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNoded
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


        # Iterative
    '''Assume that we have linked list 1 → 2 → 3 → Ø, we would like to change it to Ø ← 1 ← 2 ← 3.
	'''
	public ListNode reverseList(ListNode head) {
	    ListNode prev = null;
	    ListNode curr = head;
	    while (curr != null) {
	        ListNode nextTemp = curr.next;
	        curr.next = prev;
	        prev = curr;
	        curr = nextTemp;
	    }
	    return prev;
	}
	'''
	Time complexity : O(n)O(n). Assume that nn is the list's length, the time complexity is O(n)O(n).
	Space complexity : O(1)O(1).
    '''


    	# Recursive
    '''
		The recursive version is slightly trickier and the key is to work backwards.
		Assume that the rest of the list had already been reversed, now how do I reverse the front part?
		Let's assume the list is: n1 → … → nk-1 → nk → nk+1 → … → nm → Ø

		Assume from node nk+1 to nm had been reversed and you are at node nk.

		n1 → … → nk-1 → nk → nk+1 ← … ← nm

		We want nk+1’s next node to point to nk.

		So,

		nk.next.next = nk;

		Be very careful that n1's next must point to Ø. If you forget about this, your linked list has a cycle in it.
		This bug could be caught if you test your code with a linked list of size 2.

	'''
		public ListNode reverseList(ListNode head) {
		    if (head == null || head.next == null) return head;
		    ListNode p = reverseList(head.next);
		    head.next.next = head;
		    head.next = null;
		    return p;
		}
	'''
		Time complexity : O(n)O(n). Assume that nn is the list's length, the time complexity is O(n)O(n)
		Space complexity : O(n)O(n). The extra space comes from implicit stack space due to recursion.
		The recursion could go up to nn levels deep.
    '''