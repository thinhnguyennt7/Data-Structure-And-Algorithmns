# You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks,
#  the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are
#  a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project
#  that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies 
#  and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's
#  suspicions. 

# You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where
#  0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

# Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your
# remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable
# (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal
# directions; no diagonal moves are allowed.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int) maze = [   [0, 1, 1, 0],
					 # [0, 0, 0, 1],
					 # [1, 1, 0, 0],
					 # [1, 1, 1, 0]]
# Output:
#     (int) 7

# Inputs:
#     (int) maze =   [[0, 0, 0, 0, 0, 0],
 					# [1, 1, 1, 1, 1, 0],
 					# [0, 0, 0, 0, 0, 0],
 					# [0, 1, 1, 1, 1, 1],
 					# [0, 1, 1, 1, 1, 1],
 					# [0, 0, 0, 0, 0, 0]]
# Output:
#     (int) 11

# def toValue(r, c):
#   return r * w + c
# def toCoord(val, arrayLen):
#   return [int(val / arrayLen), val % arrayLen]
from collections import deque
def isInBound(r, c, h, w):
	return 0 <= r < h and 0 <= c < w
def shortest_path(srcR, srcC, maze):
	h, w = len(maze), len(maze[0])	
	q = deque([(srcR, srcC)])	
	shortest_len = [[-1 for _ in range(w)] for _ in range(h)]
	shortest_len[srcR][srcC] = 1
	# print(shortest_len)
	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	while len(q) > 0:
		curR, curC = q.popleft()
		# print("58", curR, curC)
		for dR, dC in dirs:
			newR, newC = curR + dR, curC + dC
			if not isInBound(newR, newC, h, w): 
				continue
			if shortest_len[newR][newC] == -1:
				shortest_len[newR][newC] = shortest_len[curR][curC] + 1
				if maze[newR][newC] == 0: 
					q.append((newR, newC))
	return shortest_len
def answer(maze):
	h, w = len(maze), len(maze[0])	
	#
	shortest_len_src = shortest_path(0, 0, maze)
	shortest_len_dst = shortest_path(h - 1, w - 1, maze)
	min_len = h * w
	for r in range(h):
		for c in range(w):
			if shortest_len_src[r][c] != -1 and shortest_len_dst[r][c] != -1:
				min_len = min(min_len, shortest_len_src[r][c] + shortest_len_dst[r][c] - 1)
	return min_len

# 	arrLen = len(number)
# 	print() arrLen
print(answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))


