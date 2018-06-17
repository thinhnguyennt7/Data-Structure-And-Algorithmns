'''
Write a program which takes as its input a String and returns
the length of the longest
substring that does not contain any repeated characters.

Example: Given the string "abcabcbb", the longest substring with no
repeated characters is "abc",

so the program would return a value of 3. Given the string "aaaaaaaa",
the longest non-repeating substring is

"a" and thus the output would be 1.
'''

def longest_nonRepating_substring(str):
	# Edge case
	if len(str) == 0:
		return 0

	maxlength = 0
	tempString = ""
	output = ""

	for i in str:
		if i not in tempString:
			tempString += i
			if len(tempString) > maxlength:
				maxlength = len(tempString)
				output = tempString
		else:
			# Find the character that repeat and then get all character from the next character to the end
			# and then + the repeated character. Repeate this step till the end.
			tempString = tempString[tempString.index(i)+ 1:] + i
	return maxlength, output

# Driver Test case
if __name__ == "__main__":
	input1 = "abcabcbb"
	input2 = "aaaaaaaa"
	input3 = ""
	input4 = "abcdedeeeeeddddeee"
	print("Output1: ", longest_nonRepating_substring(input1))
	print("Output2: ", longest_nonRepating_substring(input2))
	print("Output3: ", longest_nonRepating_substring(input3))
	print("Output4: ", longest_nonRepating_substring(input4))
