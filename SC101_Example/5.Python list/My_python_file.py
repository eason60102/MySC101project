EXIT = -1


def main():
	print('Hello, world!')
	stack = []
	stack2 = []
	while True:
		line = input('Give me lines (I will give them back reversely): ')
		if line == str(EXIT):
			break
		stack.append(line)
	
	while len(stack) != 0:
		ele = stack.pop()
		print(ele)
if __name__ == '__main__':
	main()