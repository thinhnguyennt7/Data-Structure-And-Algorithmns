# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct 
# ways can you climb to the top?

# Note: Given n will be a positive integer.


# Example 1:

# Input: 2
# Output:  2
# Explanation:  There are two ways to climb to the top.

# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output:  3
# Explanation:  There are three ways to climb to the top.

# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# DP, timeO(n), space O(n)
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        arr = [0] * (n+1)
        arr[1] = 1
        arr[2] = 2
        
        for i in range(3,n+1):
            arr[i] = arr[i-1] + arr[i-2]
            
        return arr[n]


# Fibonacci , time O(n) , space O(1)
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        first = 1
        last = 2
        mid = 0
        for i in range(3, n + 1):
            mid = first + last
            first = last
            last = mid
            
        return last
