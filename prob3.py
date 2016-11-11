
class ArrayStack:
	""" LIFO stack implementation usinng Python list as underlying storage """

	def __init__ (self,size = 1):
		""" Creat an empty stack """
		self._data = []
		self._top = -1
		self._size = size

	def len (self):
		""" Return the number of elements in the stack """
		return len (self._data)
	
	def is_empty (self):
		""" Return True if the stack is empty """
		return len(self._data) == 0

	def push (self, e):
		if self._top>=(self._size-1):
			print("Stack overflow")
		else:	
				self._data.append(e)
				self._top +=1

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



def test_stack():
	size = 5
	st = ArrayStack(size)
	st.push(10)
	st.push(20)
	st.push(30)
	st.push(40)
	st.push(50)	
	st.push(60)
	


if __name__ == '__main__':
	#test_empty_stack()
	#test_one_element_stack()
	test_stack()