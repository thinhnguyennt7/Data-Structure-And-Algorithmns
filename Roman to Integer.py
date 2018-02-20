# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range (len(s)):
            if (i == len(s) - 1):
                result = result + d[s[i]]
            else:
                if d[s[i]] < d[s[i+1]]:
                    result = result  - d[s[i]]
                else:
                    result = result + d[s[i]]
        return result



# Test Casae: "DCXXI"

# => 621