'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

def simplifyPath(path):
	"""
	:type path: str
	:rtype: str
	"""
	result = []
	elements = path.split('/')
	print("element: ", elements)
	for element in elements:
		if element == '' or element == '.':
			continue
		if element == '..':
			if result:
				result.pop()
		else:
			result.append(element)

	return '/' + '/'.join(result)

print("Solution: ", simplifyPath("/home//foo/"))