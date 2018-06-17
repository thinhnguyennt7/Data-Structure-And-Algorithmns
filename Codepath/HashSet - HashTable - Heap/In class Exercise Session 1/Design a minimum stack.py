'''

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
These are the operations you should implement for this data structure.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
get_min() -- Retrieve the minimum element in the stack.

'''

# class MinStack:
# 	def __init__(self):
# 		self.stack_list = []

# 	def push(self, x):
# 		curr_min = self.stack_list[-1][1] if self.stack_list else x
# 		if curr_min > x:
# 			curr_min = x
# 		self.stack_list.append((x, curr_min))

# 	def pop(self):
# 		if self.stack_list:
# 			self.stack_list.pop()

# 	def top(self):
# 		if self.stack_list:
# 			return self.stack_list[-1][0]
# 		return None

# 	def get_min(self):
# 		if self.stack_list:
# 			return self.stack_list[-1][1]
# 		return None


class MinStack:
	def __intit__(self):
		self.stack = []

	def push(self, element):

	def pop(self):
		getLen = len(self.stack)-1
		self.stack = self.stack[::getLen]
		return self.stack[getLen]

	def top(self):
		getLen = len(self.stack)-1
		return self.stack[getLen]

	def get_min(self):
