class LeakyStack:

	def __init__(self):
		self._data = []
		self.size = 0
		self._max = 5

	def push(self,element):
		if self.size < self._max:
			self._data.append(element)
			self.size += 1
		else:
			self.leakelement(element);


	def pop(self):
		if self.size >= 0:
			self.size -= 1
			print(self.size)
			return self._data.pop()

	def leakelement(self,element):
		temp = LeakyStack()
		for i in range(len(self._data)-1):
			temp.push(self._data.pop())
		temp.display()
		self._data.pop()
		self.size = 0
		for i in range(temp.size):
			self.push(temp.pop())
		self.push(element)
		self.display()

	def display(self):
		print(self._data)

def main():
	stack = LeakyStack()
	stack.push(10)
	stack.push(20)
	stack.push(30)
	stack.push(40)
	stack.push(50)
	stack.push(60)
main()
