class LinkedQueue:

	class _Node:
		""" Non public class for storing element in Queue """
		def __init__(self,e):
			self._element = e
			self._next = None

	def __init__(self):
		""" Create an empty Queue """
		self._head = None		
		self._tail = None
		self._length = 0

	
	def len(self):
		""" Return number of elements in the Queue """
		return self._length

	def is_empty(self):
		""" return True is Queue is empty """
		return self.len() == 0


	def first (self):
		""" Return (but do not remove) the first element in the Queue """
		if self.is_empty():
			print ("Empty Queue")
		else:
			return self._head._element

	def enqueue(self, e):
		""" Add element into Queue """
		
		newnode = self._Node(e)
		if self.is_empty():
			self._head = newnode
		else:
			self._tail._next = newnode
		self._tail = newnode		
		self._length += 1
	
	def dequeue (self):
		""" Delete element from Queue """

		if self.is_empty():
			print ('Empty Queue')
		else:
			answer = self._head._element
			self._head = self._head._next
			self._length -= 1
			if self._head is None:
				self._tail = None
			return answer
			

