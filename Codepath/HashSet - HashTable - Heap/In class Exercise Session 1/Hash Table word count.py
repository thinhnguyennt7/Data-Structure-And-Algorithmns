import re

def multimap(dictionary):
	dict = {}
	for word, count in dictionary.items():
		if count not in dict:
			dict[count] = [word]
		else:
			dict[count] += [word]

	return dict


def word_count(string):

	# Take care the special characters and lower case avoid insensitive case
	string = re.sub('[^A-Za-z]', ' ', string).lower()

	array = string.split()
	dictionary = {}
	for i in array:
		if i in dictionary:
			dictionary[i] += 1
		else:
			dictionary[i] = 1

	out = multimap(dictionary)

	return out


print(word_count("To be or not to be, that is the question"))
