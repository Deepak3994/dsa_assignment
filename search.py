class Queue:

	DEFAULTY_CAPACITY = 2

	def __init__(self):
		self._qdata = [None] * Queue.DEFAULTY_CAPACITY
		self.size = 0
		self._front = 0

	def enqueue(self,element):
		if self.size == len(self._qdata):				# if queue elements == queue capacity, allow queue capacity to grow 2* present capacity
			self._resize(2 * len(self._qdata))
		avail = (self._front + self.size) % len(self._qdata)
		self._qdata[avail] = element
		self.size += 1

	def dequeue(self):
		if self.is_empty():
			print('Queue is empty')
		else:			
			answer = self._qdata[self._front]
			self._qdata[self._front] = None
			self._front = (self._front + 1) % len(self._qdata)
			self.size -= 1
			if 0 < self.size < len(self._qdata) // 4:
				self._resize(len(self._qdata) // 2)
			return answer

	def _resize( self, cap):
		""" Resize to a new list of capacity >= len(self) """

		old = self._qdata
		self._qdata = [None] * cap
		walk = self._front
		for k in range(self.size):
			self._qdata[k] = old[walk]
			walk = (1 + walk) % len(old)
		self._front  

	def is_empty(self):
		""" Return True if the queue is empty """
		return self.size == 0



class stack:

	def __init__(self):
		self._data = []

	def push(self,element):
		self._data.append(element)

	def pop(self):
		return self._data.pop()

	def search(self,key):
		q = Queue()
		count = 0
		self.flag = 0
		
		print(self._data)
		
		for i in range(len(self._data)):
			q.enqueue(self._data.pop())
			count += 1
		print(self._data)
		
		for i in range(count):
			element = q.dequeue()
			if element == key:
				self.flag = 1
				self._data.append(element)
			else:
				self._data.append(element)
		
		print(self._data)
		count = 0
		for i in range(len(self._data)):
			q.enqueue(self._data.pop())
			count += 1

		for i in range(count):
			self._data.append(q.dequeue())

		print(self._data)
		return(self.flag)

def main():
	s = stack()
	s.push(10)
	s.push(20)
	s.push(30)
	s.push(40)
	assert(s.search(10) == 1)
	assert(s.search(100) == 0)

main()
	




