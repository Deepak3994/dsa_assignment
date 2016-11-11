class SingleList:

	class _Node:
		""" Non public class for storing element in SingleList """
		def __init__(self,e):
			self._element = e
			self._next = None


	def __init__(self):
		""" Create an empty SingleList """
		self._head = None
		self._tail = None
		self._length = 0

	
	def len(self):
		""" Return number of elements in the list """
		return self._length


	def is_empty(self):
		""" Return True is list is empty """
		return self.len() == 0


	def first (self):
		""" Return (but do not remove) the first element (head position) in the list """
		if self.is_empty():
			print ("Empty List")
		else:
			return self._head._element


	def add_first(self, e):
		""" Add an element at the start (head) of SingleList """		
		newnode = self._Node(e)
		if self.is_empty():
			self._head = self._tail = newnode
		else:
			newnode._next = self._head
			self._head = newnode				
		self._length += 1


	def add_last (self, e):
		""" Add an element at the end (tail) of SingleList """		
		newnode = self._Node(e)
		if self.is_empty():
			self._tail = self._head = newnode
		else:
			self._tail._next = newnode
			self._tail = newnode
		self._length += 1
		

	def lookup (self, key):
		""" Search for element 'key' in SingleList """
		current = self._head		
		while current is not None:
			if current._element == key :
				break
			else:
				current = current._next

		return current != None

	
	def delete_first (self):		
		""" Delete first (head) element from SingleList """
		if self.is_empty():
			print ('Empty List')
		else:
			self._head = self._head._next
			self._length -= 1
			if self._head is None:
				self._tail = None


