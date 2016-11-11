class Stack:
	def __init__(self):		
	    self._data = []

	def push(self,x):
		self._data.append(x)

	def pop(self):
		if(self.is_empty()):
			print("stack is empty")
		else:
		    return self._data.pop()

	def is_empty(self):
		return len(self._data) == 0

	def copy_reverse(self, T):
	    for x in range(len(temp1)):
	        T.push(self.pop())

	    print(T._data)	
	    

	    
if __name__ == '__main__':
	S = Stack()
	T = Stack()
	S.push(5)
	S.push(10)
	S.copy_reverse(T)
		
