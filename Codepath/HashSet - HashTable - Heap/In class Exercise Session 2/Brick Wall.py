'''
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the

same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick
in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw
the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Example:
Input:
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]

Output: 2

Note:
The width sum of bricks in different rows are the same and won't exceed INT_MAX.
The number of bricks in each row is in range [1,10,000]. The height of wall is in range

[1,10,000]. Total number of bricks of the wall won't exceed 20,000.


Bricks in rows align with each other when the total
    length of the bricks so far match. For example,
    a row that begins with [1, 2] would align with another row
    that begins [2, 1], because both have a total sum of 3 at
    that point.
    We are interested in the cumulative sum of brick
    lengths for each row. We know when these cumulative sums
    match, we do not cut through those bricks at that point.
    Furthermore, we can ignore the last brick
    in every row since all rows are the same length and we cannot
    cut at the end.
    We thus maintain the numbers of rows that have each cumulative sum
    amount, and can thus obtain the number of rows we are not cutting
    through for each place to cut. By subtracting this number from
    the total number of rows, we get the number of bricks that
    are cut through. We therefore look for the
    cumulative sum with the most number of aligned bricks.

    >>> least_bricks([[1,2,2,1], [3,1,2], [1,3,2], [2,4], [3,1,2], [1,3,1,1]])
    2
'''
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
            counts = defaultdict(int)
		    for row in wall:
		        total = 0
		        for brick in row[:-1]:
		            total += brick
		            counts[total] += 1
		    if len(counts) == 0:
		        return len(wall)
		    return len(wall) - max(counts.values())