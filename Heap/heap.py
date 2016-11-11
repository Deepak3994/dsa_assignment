
class Empty(Exception):
	""" Error attempting to access an element from an empty container """
	def __init__(self, args):
		self._args = args

class Heap:

	""" Non public behaviors
	"""
	# Given the index 'j', return the index of parent
	def __parent(self, j):
		return (j - 1) // 2

	# Return the index of left child for node at 'j'
	def __left(self, j):		
		return 2 * j + 1

	# Return the index of right child for node at 'j'
	def __right(self, j):
		return 2 * j + 2

	# Return true if node at 'j' has left child
	def __has_left(self, j):
		return self.__left(j) < len(self._data)

	# Return true if node at 'j' has right child
	def __has_right(self, j):
		return self.__right(j) < len(self._data)

	# Swap the values at given indices
	def __swap(self, i, j):		
		self._data[i], self._data[j] = self._data[j], self._data[i]

	# Move the node at 'j' recursively up if value is less than parent
	def __upheap(self, j):
		parent = self.__parent(j)
		
		if j > 0 and self._data[j] < self._data[parent]:
			self.__swap(j, parent)
			self.__upheap(parent)

	# Pull the node down from index'j' if value is greater than value of children
	def __downheap(self, j, size):
		if self.__left(j) < size:	# check whether node at 'j' has left child	
			left = self.__left(j)
			small_child = left
		
			if self.__right(j) < size:	# check whether node at 'j' has right child		
				right = self.__right(j)
				if self._data[right] < self._data[left]:
					small_child = right
			if self._data[small_child] < self._data[j]:
				self.__swap(j, small_child)
				self.__downheap(small_child, size)
	
	# Build Minimum heap with least valued node at root
	def __buildheap(self):

		length = self.__len__() 
		start = (length-2)  // 2
		for j in range(start , -1, -1):
			self.__downheap(j, length )

	def __testsort(self):
		for i in range(0, len(self._data) - 1):
			assert(self._data[i] >= self._data[i+1])


	""" public behaviors
	"""

	def __init__(self, lst=[]):
		""" create a new empty queue """
		self._data = lst
		self.__buildheap()

	def __len__(self):
		return len(self._data)

	# Add a node to Heap
	def add(self, key):		
		self._data.append(key)
		self.__upheap(len(self._data) - 1)

	# Return minimum value from heap
	def min(self):		
		if self.is_empty():
			try:
				raise Empty('Heap is Empty')
			except Empty as err:
				print(err._args)
		else:
			return self._data[0]
			
	
	# Remove min valued node from heap and restore heap property
	def remove_min(self):		
		if self.is_empty():
			try:
				raise Empty('Heap is Empty')
			except Empty as err:
				print(err._args)
		else:
			self.__swap(0, len(self._data) - 1)
			item = self._data.pop()
			self.__downheap(0, len(self._data) - 1 )
			return (item)

	def is_empty(self):
		return len(self._data) == 0

	# Sort in descending order
	def heap_sort(self):
		length = len(self._data)
		for i in range(length-1, -1, -1):
			self.__swap(0, i)
			self.__downheap(0, i)
		self.__testsort()


	def print_elements(self):
		print (self._data)

	def test_heap_order(self):
		for i in range(len(self._data) - 1, 0, -1 ):			
			assert(self._data[i] >= self._data[self.__parent(i)])

