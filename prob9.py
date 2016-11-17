#9. Design a double-ended queue using two stacks as instance variables.
class stack:
	def __init__(self):
		self._data = []

	def push(self,ele):
		self._data.append(ele)

	def pop(self):
		return self._data.pop()

	def length(self):
		return len(self._data)

	def display(self):
		print(self._data)

class queue:
	def __init__(self):
		self.s1 = stack()
		self.s2 = stack()


	def enqueue_rear(self,ele):
		if self.s2.length() == 0:
			self.s2.push(ele)
		else:
			self.s1.push(self.s2.pop())
			self.s1.push(ele)
			for i in range(self.s1.length()):
				self.s2.push(self.s1.pop())
		#self.s2.display()

	def dequeue_front(self):
		return self.s2.pop()

	def enqueue_front(self,ele):
		self.s2.push(ele)

	def dequeue_rear(self):
		for i in range(self.s2.length()):
			self.s1.push(self.s2.pop())
		ele = self.s1.pop()
		for i in range(self.s1.length()):
			self.s2.push(self.s1.pop())
		return ele


def main():
	q = queue()
	q.enqueue_rear(10)
	q.enqueue_front(20)
	q.enqueue_rear(30)
	q.enqueue_front(40)
	print(q.dequeue_front())
	print(q.dequeue_rear())
	

main()