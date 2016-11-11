class Stack:
	def __init__(self):		
	    self._data = []
	    self._size = 0

	def push(self,x):
		self._data.append(x)
		self._size += 1

	def pop(self):
		if(self.is_empty()):
			print("stack is empty")
		else:
			self._size -= 1
			return self._data.pop()

	def is_empty(self):
		return len(self._data) == 0

	def display(self):
		print(self._data)

def operations():
	R = Stack()
	S = Stack()
	T = Stack()

	R.push(1)
	R.push(2)
	R.push(3)
	R.display()
	
	S.push(4)
	S.push(5)
	S.display()

	T.push(6)
	T.push(7)
	T.push(8)
	T.push(9)
	T.display()

	while S.is_empty() == 0:
		(R.push(S.pop()))
		count += 1
	while T.is_empty() == 0:
		(R.push(T.pop()))
		count += 1
	R.display()

if __name__ == '__main__':
	operations()