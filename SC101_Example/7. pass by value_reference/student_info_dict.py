"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'students_info.txt'


def main():
	all_d = {}  # 記憶體位置 0x111
	# d_student = {}  # 不能放這, 不然只有會一棟房子 0x222
	#####################法2
	with open(FILE, 'r') as f:
		for line in f:
			tokens = line.split()
			all_d[tokens[0]] = {'Age': int(tokens[1]), "EMAIL": tokens[2], "FOOD": tokens[3:]}
	######################
	#####################法1
	'''
	with open(FILE, 'r') as f:
		for line in f:
			tokens = line.split()
			name = tokens[0]
			age = int(tokens[1])
			email = tokens[2]
			food = tokens[3:]
			# d_student = {'Age': age, 'EMAIL': email, 'FOOD': food}  # 法2
			d_student = {} # 記憶體位置 0x222/0x333...
			# print(d_student)  # {}, 傳內容
			# print(id(d_student))  # id傳記憶體位置,但會回傳10進制
			print(hex(id(d_student)))  # Allocate, 傳16進制的記憶體位置
			d_student['Age'] = age
			d_student['EMAIL'] = email
			d_student['FOOD'] = food
			all_d[name] = d_student  # 記憶體位置 0x222/0x333...
	'''
	######################
	print_out_d(all_d)


def print_out_d(d):
	"""
	: param d: (dict) key of type str is the name of student
				value of type dict is the info of the student
	---------------------------------------------------------------
	This function prints out a nested data structure on console
	"""
	for student, student_info in d.items():
		print(student)
		print(student_info)
		print('-'*80)


if __name__ == '__main__':
	main()