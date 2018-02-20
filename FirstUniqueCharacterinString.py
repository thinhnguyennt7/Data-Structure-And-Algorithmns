# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

#Not Optimize
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if (len(s) == 0):
            return - 1
        j = 0
        for i in s:
            if i not in s[:j] + s[j+1:]:
                return j
            else:
                j = j + 1
        return -1

#Optimize Hash Table 
class Solution:
    def firstUniqChar(self, string):
        """
        :type s: str
        :rtype: int
        """
        # Keep adding keys and values to the hash table
        dictionary = {}
        for char in string:
            if char in dictionary.keys():
                dictionary[char] += 1
            else:
                dictionary[char] = 1

        # Check and return
        for i in range(len(string)):
            if dictionary[string[i]] == 1:
                return i

        return -1
