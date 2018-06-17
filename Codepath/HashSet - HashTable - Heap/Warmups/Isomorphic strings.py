'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character but a character may
map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

'''
class Solution:
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if len(s) < len(t):
			return False

		begin = 0
		end = len(t) - 1
		dictionary = dict()

		while begin <= end:
			if s[begin] in dictionary:
				if dictionary[s[begin]] != t[begin]:
					return False
			else:
				if t[begin] in dictionary.values():
					return False
				dictionary[s[begin]] = t[begin]

		return True
