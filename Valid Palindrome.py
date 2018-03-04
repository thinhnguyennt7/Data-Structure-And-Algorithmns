# Given a string, determine if it is a palindrome, considering only alphanumeric
# characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask
# during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.


# By recursive
import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^0-9a-zA-Z]', '', s).lower()
        return self.palindromeRecur(s)
        
    def palindromeRecur(self, string):
        if len(string) == 0 or len(string) == 1:
            out = True
        else:
            if string[0] == string[len(string)-1]:
                out = self.palindromeRecur(string[1:len(string)-1])
            else:
                out = False
        
        return out
                

# By loop
import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^0-9a-zA-Z]', '', s).lower()
        i = 0
        j = len(s) - 1
        
        if len(s) == 0 or len(s) == 1:
            return True
        while i < len(s):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
                
        return True