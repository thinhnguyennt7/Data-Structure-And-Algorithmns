
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output:  321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only hold integers 
# within the 32-bit signed integer range.
# For the purpose of this problem, assume that your function returns 0
# when the reversed integer overflows.


class Solution(object):
    def reverse(self, x):
        
        # Set the negative and positive overflow points
        negativeOverflow = -2 ** 31
        postiveOverflow = (2 ** 31) - 1

        newInt = 0
        negativeFlag = False
        
        # If the value is negative
        if x < 0 :
            x = x * -1
            negativeFlag = True
        
        while (x > 0):
            newInt = newInt * 10 + x % 10
            x = x / 10
            
        if negativeFlag:
            newInt = newInt * -1
        
        # Check overflow
        if (newInt > postiveOverflow) or (newInt < negativeOverflow):
            return 0
            
        return newInt
    