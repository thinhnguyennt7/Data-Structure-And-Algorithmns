# Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and
# pattern - and should return true if the text matches the pattern as a regular expression. For simplicity, assume that the actual symbols
#  '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.
#
# In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' is
# treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter (see
# fourth and fifth examples). For more information on regular expression matching, see the Regular Expression Wikipedia page.
#
# Explain your algorithm, and analyze its time and space complexities.


# Examples:
# input:  text = "aa", pattern = "a"
# output: false
#
# input:  text = "aa", pattern = "aa"
# output: true
#
# input:  text = "abc", pattern = "a.c"
# output: true
#
# input:  text = "abbb", pattern = "ab*"
# output: true
#
# input:  text = "acd", pattern = "ab*c."
# output: true


def isMatch(text, pattern):
    return isMatchHelper(text, pattern, 0, 0)

def isMatchHelper(text, pattern, firstPointer, secondPointer):
    if firstPointer >= len(text):
        return True



isMatch("", "")


















# def is_match(text, pattern):
#   # Set the pointers
#     a_Pointer = 0
#     b_Pointer = 0
#
#     #Check if the length of text and pattern if equal 0
#     if len(text) == 0 and len(pattern) == 0:
#         return True
#     elif len(text) == 0 or len(pattern) == 0:
#         if '*' in pattern:
#             return True
#
#           # Run two pointers
#     while a_Pointer < len(text) and b_Pointer < len(pattern):
#
#       # if the char in text and pattern are same or it is '.'
#         if text[a_Pointer] == pattern[b_Pointer] or pattern[b_Pointer] == '.':
#           #Increment
#             a_Pointer += 1
#             b_Pointer += 1
#         else:
#           # If the char is the *
#             if pattern[b_Pointer] == '*':
#               # Set the old char
#                 pervious = pattern[b_Pointer - 1]
#                 #Compare the var with the current text at the pointer
#                 if text[a_Pointer] == pervious:
#                     a_Pointer += 1 # increment
#                  # IF the var not same as the current pointer of text.
#                 else:
#                     b_Pointer += 1 # increment B pointer
#             else:
#                 if pattern[b_Pointer + 1] == '*': # if the next char is *
#                     b_Pointer += 2 #increment pointer by 2
#                 else:
#                     return False
#
#            # Make sure it run entire string
#         if a_Pointer == len(text) - 1 and b_Pointer == len(pattern) - 1:
#             return True
#
#     return False

# Regular for loop
# def is_match(text, pattern):
#     a_Pointer = 0
#     b_Pointer = 0
#     if len(text) == 0 and len(pattern) == 0:
#         return True
#     elif len(text) == 0 or len(pattern) == 0:
#         if '*' in pattern:
#             return True
#
#     while a_Pointer < len(text) and b_Pointer < len(pattern):
#         if text[a_Pointer] == pattern[b_Pointer] or pattern[b_Pointer] == '.':
#             a_Pointer += 1
#             b_Pointer += 1
#         else:
#             if pattern[b_Pointer] == '*':
#                 pervious = pattern[b_Pointer - 1]
#                 if text[a_Pointer] == pervious:
#                     a_Pointer += 1
#                 else:
#                     b_Pointer += 1
#             else:
#                 if pattern[b_Pointer + 1] == '*':
#                     b_Pointer += 2
#                 else:
#                     return False
#
#         if a_Pointer == len(text) - 1 and b_Pointer == len(pattern) - 1:
#             return True
#
#     return False

# print(is_match("a", ".*.*.*.*a"))



# Recursion
# def isMatch(text, pattern):
#     return isMatchHelper(text, pattern, 0, 0)

 #
 # Input:
 #   text - the text to check,
 #   pattern - the regular expression to be checked,
 #   textIndex - the index the text is checked from
 #   patIndex -  the index the pattern is checked from
 # Output:
 #  true if the text from the index textIndex matches
 #  the regular expression pattern from the pattern Index.
 #  E.g. isMatchHelper(“aaabb”,”cab*”,2, 1) since the text
 #  from index 2 (“abb”) matches the pattern from index 1 (“ab*”)

# def isMatchHelper(text, pattern, textIndex, patIndex):
#     print("83", textIndex)
#     print("84", patIndex)
#     # base cases - one of the indexes reached the end of text or pattern
#     if (textIndex >= len(text)):
#         if (patIndex >= len(pattern)):
#             return True
#         else:
#             if (patIndex+1 < len(pattern)) and  (pattern[patIndex+1] == '*'):
#                 print("91", pattern[patIndex+1])
#                 return isMatchHelper(text, pattern, textIndex, patIndex + 2)
#             else:
#                 return False
#
#     elif (patIndex >= len(pattern)) and (textIndex < len(text)):
#         return False
#
#     # string matching for character followed by '*'
#     elif (patIndex+1 < len(pattern)) and (pattern[patIndex+1] == '*'):
#         print("101", pattern[patIndex+1])
#         if (pattern[patIndex] == '.') or (text[textIndex] == pattern[patIndex]):
#             print("103", pattern[patIndex])
#             return (isMatchHelper(text, pattern, textIndex, patIndex + 2) or
#                     isMatchHelper(text, pattern, textIndex + 1, patIndex))
#         else:
#             return isMatchHelper(text, pattern, textIndex, patIndex + 2)
#
#     # string matching for '.' or ordinary char.
#     elif (pattern[patIndex] == '.') or (pattern[patIndex] == text[textIndex]):
#         return  isMatchHelper(text, pattern, textIndex + 1, patIndex + 1)
#     else:
#         return False
#
# print(isMatch("bbbbbbbb", ".*.*.*.*a"))
