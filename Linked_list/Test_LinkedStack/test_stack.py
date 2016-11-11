from StackLinked import Linked_Stack 


def test_empty_stack():
	s = Linked_Stack.LinkedStack()
	assert (s.len() == 0)
	

def test_one_element_stack():
	s = Linked_Stack.LinkedStack()
	s.push(10)
	assert (s.len() == 1)	
	assert (s.peek() == 10)
	s.pop()
	assert (s.is_empty())


def test_multi_element_stack():
	s = Linked_Stack.LinkedStack()
	for e in range(10):
		s.push(e)

	assert(s.len() == 10)
	s.pop()
	assert (s.len() == 9)
	assert (s.peek() == 8)



if __name__ == '__main__':
	test_empty_stack()
	test_one_element_stack()
	test_multi_element_stack()
	
