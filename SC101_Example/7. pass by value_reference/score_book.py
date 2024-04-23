"""
File: score_book.py
Name: 
----------------------
This program shows how to use a Python
dict by implementing a score book
"""

# This controls when to break the loop for user inputs
QUIT = ''


def main():
	"""
	This main function contains 3 functions that
	constructing a score book. d is passed by reference
	"""
	d = {}
	get_scores(d)
	check_score(d)
	print_scores(d)
	

def get_scores(d):
	"""
	: param d: (dict) an empty python dict 
	--------------------------------------
	This function puts key->value pairs in d
	"""
	print("Let's input some data!")
	while True:
		name = input('Name: ')
		if name == QUIT:
			break
		else:
			score = int(input('Score: '))
			d[name] = score


def check_score(d):
	"""
	: param d: (dict) a python dict contains name->score
	--------------------------------------
	This checks if key in d
	"""
	print("Let's check the score!")
	while True:
		name_to_check = input('Name to check: ')
		if name_to_check == QUIT:
			break
		if name_to_check in d:
			print(d[name_to_check])  # key error
		else:
			print(f'There is no {name_to_check} in d.')
	

def print_scores(d):
	"""
	: param d: (dict) a python dict contains name->score
	--------------------------------------
	This function prints out all the key-value pairs
	"""
	print('-----------------------')
	for student, student_score in d.items():
		print(student, '->', student_score)


if __name__ == '__main__':
	main()
