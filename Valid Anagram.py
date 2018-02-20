# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# Used sorted
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        newAna = sorted(t)
        newString = sorted(s)
        if (newAna == newString):
            return True
        else:
            return False

# Used hash map
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Add char from original string to hash map
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1 # if not in dict then add and set equal 1
            else:
                dict[i] += 1 # if already in dict then incremnet by 1

        # Check char from new string with hash map
        for o in t:
            if o not in dict:
                return False
            else:
                dict[o] -= 1

        # Check if the values in map not equal 0 return False, else return True
        for num in dict.values():
            if num != 0:
                return False

        return True
