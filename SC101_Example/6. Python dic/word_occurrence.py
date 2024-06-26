"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
	with open(FILE, 'r') as f:
		word_d = {}
		for line in f:
			tokens = line.split()
			for token in tokens:
				token = string_manipulation(token)
				if token not in word_d:
					word_d[token] = 1
				else:
					# word_d[token] = word_d[token] +1
					word_d[token] += 1
		print_out_d(word_d)


def string_manipulation(s):
	ans = ''
	for ch in s:
		# if ch.isalpha():
		if ch not in PUNCTUATION:
			ans += ch.lower()
	return ans


def print_out_d(d):
	"""
	: param d: (dict) key of type str is a word
					value of type int is the word occurrence
	---------------------------------------------------------------
	This function prints out all the info in d
	"""
	for word, occurrence in sorted(d.items(), key=lambda t: t[1]):
		# [('a',100), ('the', 300), ('romeo', 30),...)
		print(word, '->', occurrence)


if __name__ == '__main__':
	main()
