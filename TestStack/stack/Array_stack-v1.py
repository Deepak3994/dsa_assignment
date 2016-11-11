class Empty (Exception):
	""" Error attempting to access an element from an empty container """
	pass


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

		Raise Empty exception if the Stack is empty
		"""
		if self.is_empty():
			try:
				raise Empty('Stack is empty')
			except Empty as error:
				print ('Hi no element')
		else:
			return self._data[-1]

	def pop (self):
		""" Remove and return the element from the top of the stack
		Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			try:
				raise Empty('Stack is empty')
			except Empty as error:
				print ('Empty stack')
		else:
			return self._data.pop()



def test_empty_stack():
	st = ArrayStack()	
	print (st.top())


def test_stack():
	st = ArrayStack()	
	print (st.top())
	st.push(10)
	st.push(20)
	st.pop()
	st.pop()
	st.pop()
	
	print (st.len())


if __name__ == '__main__':
	test_empty_stack()
