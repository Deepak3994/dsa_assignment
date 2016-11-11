

class ArrayStack:
	""" LIFO stack implementation usinng Python list as underlying storage """

	def __init__ (self):
		""" Creat an empty stack """
		self._data = []

	def len (self):
		""" Return the number of elements in the stack """
		return len (self._data)
	
	def is_empty (self):
		""" Return True if the stack is empty """
		return len(self._data) == 0

	def push (self, e):
		""" Add element e to the top of the Stack """
		self._data.append(e)

	def top (self):
		""" Return (but do not remove) the element at the top of the stack 

		"""
		if self.is_empty():
			print('Stack is empty')
		else:
			return self._data[-1]

	def pop (self):
		""" Remove and return the element from the top of the stack
		"""
		if self.is_empty():
			print('Stack is empty')			
		else:
			return self._data.pop()



def test_empty_stack():
	st = ArrayStack()	
	st.top()
	
def test_one_element_stack():
	st = ArrayStack()
	st.push(10)
	assert (st.top() == 10)

	st.pop()
	assert(st.is_empty())

def test_stack():
	st = ArrayStack()
	st.push(10)
	st.push(20)
	st.pop()
	st.pop()
	st.pop()
	
	assert(st.len() == 0)


if __name__ == '__main__':
	#test_empty_stack()
	#test_one_element_stack()
	test_stack()
