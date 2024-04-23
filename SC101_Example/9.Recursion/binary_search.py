def main():
	lst = [3, 6, 9, 10, 11, 23, 33, 45, 66, 99]
	print(binary_search(lst, 7))  # False
	print(binary_search(lst, 23))  #True


def binary_search(lst, target):
	"""
	:param lst: list[int], a Python list storing integers.
	:param target: int, the value to be searched.
	:returns : bool, if target is in the lst or not.
	"""
	# Your Code Here
	# 2 pointers
	low, high = 0, len(lst)-1
	while low < high:
		mid = (low+high) // 2
		if target == lst[mid]:
			return True
		elif target > lst[mid]:
			low = mid + 1
		elif target < lst[mid]:
			high = mid - 1
	return False

if __name__ == '__main__':
	main()
