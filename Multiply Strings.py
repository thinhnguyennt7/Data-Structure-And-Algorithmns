"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

############## Steps Em nghĩ 
"511" * "51"

Use Stack
(1*1)x10^0 + (1*1)x10^1 + (5*1)x10^2 = 511
(1*5)x10^0 + (1*5)x10^1 + (5*5)x10^2 = 2555
 
  511
2555
------
26061
___________________________________________
Arr[i + j] += num1[i] * num2[j]

Arr = [_,_,_,_,_] length 5
i = 3
j = 2
"""

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
    	# "511" * "51"
    	finalLength = len(num1) + len(num2)
	    newArr = [0] * finalLength
	    for i in range(len(num1)-1:-1:-1):
	    	for j in range(len(num2)-1:-1:-1):
	    		newArr[i+j] += int(num1[i]) * int(num2[j])

		print(newArr)


print(multiply("511", "51"))







