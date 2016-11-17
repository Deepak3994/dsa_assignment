#15. Design an ADT for a two-color, double-stack ADT that consists of two stacks – one “red” 
#and one “blue” – and has as its operations color-coded versions of the regular stack ADT operations.
# For example, this ADT should support both a red push operation and a blue push operation. Give an 
# efficient implementation of this ADT using single array whose capacity is set at some value N that 
# is assumed to always be larger than the sizes of the red and blue stacks combined.

class Stack:
	def __init__(self):
		self.max = 10
		self._size = 0	
		self._data = [None] * self.max
		self.red_top = -1
		self.blue_top = (self.max//2) -1 	
	    

	def red_push(self,x):
		if self.red_top < self.max//2:
			self._data[self.red_top] = x
			self.red_top += 1

	def blue_push(self,x):
		if self.blue_top < self.max:
			self._data[self.blue_top] = x
			self.blue_top += 1

	def red_pop(self):
		if self.red_top < 0:
			print("red stack is empty")
		else:
			ele = self._data[self.red_top]
			self._data[self.red_top] = None
			self.red_top -= 1
			return ele

	def blue_pop(self):
		if self.blue_top < (self.max//2):
			print("blue stack is empty")
		else:
			ele = self._data[self.blue_top]
			self._data[self.blue_top] = None
			self.blue_top -= 1
			return ele

	
def main():
	s1 = Stack()
	s1.red_push(10)
	s1.blue_push(20)
	s1.display()
	s1.red_pop()
	s1.blue_pop()
	
main()