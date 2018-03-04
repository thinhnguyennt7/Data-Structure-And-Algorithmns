# Write a function that takes an unsigned integer and returns the number
#  of ’1' bits it has (also known as the Hamming weight).

# For example, the 32-bit integer ’11' has binary representation
#  00000000000000000000000000001011, so the function should return 3.


# Using bit manipulation
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        for i in range(32):
            if self.shift(n, i):
                counter += 1
        return counter
        
    def shift(self, n, i):
        mask = 1
        mask = mask << i
        if n & mask == 0:
            return False
        return True
        
