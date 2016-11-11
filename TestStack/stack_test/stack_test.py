from stack import Array_stack

def test_empty_stack():
	st = Array_stack.ArrayStack()	
	st.top()
	
def test_one_element_stack():
	st = Array_stack.ArrayStack()
	st.push(10)
	assert (st.top() == 10)

	st.pop()
	st.push(20)
	assert(st.is_empty())

def test_stack():
	st = Array_stack.ArrayStack()
	st.push(10)
	st.push(20)
	st.pop()
	st.pop()
	st.pop()
	
	assert(st.len() == 0)


if __name__ == '__main__':
	#test_empty_stack()
	test_one_element_stack()
	#test_stack()