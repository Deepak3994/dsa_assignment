class LinkedStack:

	class _Node:
		""" Non public class for storing element in Stack """
		def __init__(self,e):
			self._element = e
			self._next = None

	def __init__(self):
		""" Create an empty Stack """
		self._top = None		
		self._length = 0

	
	def len(self):
		""" Return number of elements in the Stack """
		return self._length

	def is_empty(self):
		""" return True is Stack is empty """
		return self.len() == 0


	def peek (self):
		""" Return (but do not remove) the top element in the Stack """
		if self.is_empty():
			print ("Empty Stack")
		else:
			return self._top._element

	def push(self, e):
		""" Add element into Stack """
		
		newnode = self._Node(e)
		newnode._next = self._top
		self._top = newnode
		
		self._length += 1


	
	def pop (self):
		""" Delete element from Stack """

		if self.is_empty():
			print ('Empty Stack')
		else:
			answer = self._top._element
			self._top = self._top._next
			self._length -= 1
			return answer

