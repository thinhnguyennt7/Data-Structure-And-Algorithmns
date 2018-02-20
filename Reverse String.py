
# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(arr):
            start, end = 0, len(arr) - 1
            while start < end:
                temp = arr[start]
                arr[start] = arr[end]
                arr[end] = temp
                start, end = start + 1, end - 1
                
                
        cArr = list(s)
        reverse(cArr)
        return ''.join(cArr)