# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # [0,1,2,3,4,5,2,1,9,9,10]
        # [0,1,2,3,4,5,2,2,0,0,1]
            
        for i in range(len(digits)-1,-1,-1):
            reminder = 0
            if((digits[i] + reminder + 1) >= 10):
                digits[i] = (digits[i]+1) % 10
                reminder = 1
            else:
                digits[i] += 1
                break
        if (reminder != 0):
            digits.insert(0,reminder)
            return digits
        return digits
            