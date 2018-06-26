'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

	1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
	1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# REcursive way:
# Time: O(N)
# Space: O(N)
class Solution:
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		return self.isMirror(root, root)

	def isMirror(self, root1, root2):
		if root1 == None and root2 == None:
			return True
		if root1 == None or root2 == None:
			return False

		return root1.val == root2.val and self.isMirror(root1.right, root2.left) and self.isMirror(root1.left, root2.right)

# Iterative way
# Time: O(N)
# SPACE: O(N)
	def isSymmetric(self, root):
		if not root:
			return True

		stack = [root.left, root.right]
		while stack:
			t1 = stack.pop()
			t2 = stack.pop()
			if not t1 and not t2: continue
			if not t1 or not t2: return False
			if t1.val != t2.val: return False

			stack.append(t1.left)
			stack.append(t2.right)
			stack.append(t1.right)
			stack.append(t2.left)
		return True


