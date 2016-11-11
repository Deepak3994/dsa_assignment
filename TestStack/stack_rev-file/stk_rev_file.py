
from stack import Array_stack

def test_reverse_file (filename):
	""" Overwrite given file with its contents line by line reversed """

	S = Array_stack.ArrayStack()
	original = open(filename)
	for line in original:
		S.push(line.rstrip('\n'))
	original.close()
	# now we write with contents in LIFO order

	output = open(filename, 'w')
	while not S.is_empty():
		output.write(S.pop() + '\n')
	output.close()


if __name__ == '__main__':
	test_reverse_file('sample.txt')