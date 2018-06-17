'''
Write a heap class that represents a minimum heap using an array. Implement the insert method for this min heap class.

min_heap = MinHeap()
min_heap.insert(2)
min_heap.insert(4)
min_heap.insert(1)

# Underlying array should look like: [1, 4, 2]
If time permits, implement the delete_min() method.

'''

# class MinHeap:
# 	def __init__(self):
# 		self.heap_list = []

# 	def insert(self, new_element):
# 		self.heap_list.append(new_element)
# 		self.bubble_up(len(self.heap_list) - 1)

# 	def bubble_up(self, curr_index):
# 	  parent_index = (curr_index - 1) // 2
# 	  while parent_index >= 0:
# 		curr_element, parent_element = self.heap_list[curr_index], self.heap_list[parent_index]
# 		if curr_element < parent_element:
# 			self.heap_list[parent_index] = curr_element
# 			self.heap_list[curr_index] = parent_element
# 			curr_index = parent_index
# 			parent_index = (parent_index - 1) // 2
# 		else:
# 			break
# 			
# 			
# 			


class minHeap:
	def __init__(self):
		self.heap_list = []

	def insert(self, new_element):
		self.heap_list.append(new_element)
		self.bubble_up(len(self.heap_list) - 1)

	def bubble_up(self, curr_index):
		parent_index = (curr_index - 1) // 2
		while parent_index >= 0:
			curr_element, parent_element = self.heap_list[curr_index], self.heap_list[parent_index]
			if curr_element < parent_element:
				self.heap_list[parent_index]



