'''
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj.
Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: [3, 1, 4, 2]

val = -999999999999
1. [2]

2. 2 < 4 => [2, 4] val = 2

3. 1 < 2  => True


Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


Note that it is relatively easy to break the sequence into increasing/decreasing ranges, so we can think of the sequence as an
alternating sequence of  increasing/decreasing ranges.

->>>If there exists a 132 pattern, the 13 part must be in an increasing range, and the 2 must be somewhere else after that increasing range,
so we can always make the 1 the start of the increasing range, and 3 as the end of the increasing range. So we have all the candidate 13
parts by a single scan. <<<-

The real problem is finding a 2. If we find out all the increasing range and then find the 2, we will be screwed by the quadratic performance
because there could be O(n) increasing ranges and every search take O(n) time.

The key idea is that suppose we have an increasing range [a,b] and the next value is c, c must be less than b otherwise the increasing range
simply continues. If a<c<b then we are done finding the 132 pattern, so the worst case we need to cater is c<a.

Therefore, the current set of increasing ranges should be sorted by their starting point in descending order, now whenever we find a number
a<d<b, we can declare we are done, otherwise for d<a we continue building up the increasing range, or when b≤d we can forget about
the range [a,b] because we have a better range [c,d]. We can simply manage these increasing ranges in a stack!
'''

import sys
def find132pattern(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        data = []
        value = -sys.maxsize # -9223372036854775807
        for i in nums[::-1]:
            if i < value:
                return True
            while data and data[-1] < i:
                value = data.pop()
            data.append(i)
        return False

# Driver
if __name__ == '__main__':
	input = [3, 1, 4, 2]
	print("Output: ", find132pattern(input))