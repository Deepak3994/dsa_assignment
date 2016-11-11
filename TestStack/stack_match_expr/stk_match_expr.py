
from stack import Array_stack

def test_is_matched_expression (expr):
	""" Return True if all delimiters are properly match; False otherwise. """	
	lefty = '({['
	righty = ')}]'
	S = Array_stack.ArrayStack()
	for c in expr:
		if c in lefty:
			S.push(c)
		elif c in righty:
			if S.is_empty():
				return False
			if righty.index(c) != lefty.index(S.pop()):
				return False
	
	return S.is_empty()


if __name__ == '__main__':	
	print(test_is_matched_expression('main(){ if ( x[10] == 20 ) { print(x)} }'))

