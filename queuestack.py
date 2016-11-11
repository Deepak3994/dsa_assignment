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


	def enque(self,ele):
		if self.s2.length() == 0:
			self.s2.push(ele)
		else:
			self.s1.push(self.s2.pop())
			self.s1.push(ele)
			for i in range(self.s1.length()):
				self.s2.push(self.s1.pop())
		self.s2.display()

	def dequeue(self):
		return self.s2.pop()


def main():
	q = queue()
	q.enque(10)
	q.enque(20)
	print(q.dequeue())

main()