import ArrayQueue

class TreeNode:
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def size(self):
		return self.size


	def insert(self,key,value):
		if self.root:
			self.insert_node(key,value,self.root)
		else:
			self.root = TreeNode(key,value)
		self.size += 1

	def insert_node(self,key,value,current):
		if key < current.key:
			if current.left is not None:
				self.insert_node(key,value,current.left)
			else:
				current.left = TreeNode(key,value)
		elif key > current.key:
			if current.right is not None:
				self.insert_node(key,value,current.right)
			else:
				current.right = TreeNode(key,value)

	def delete(self,key):
		if not self.root is None:
			self.delete_node(self.root,key)
	
	def delete_node(self,node,key):
		if node is None:
			return
		if key > node.key:
			node.right = self.delete_node(node.right,key)
		elif key < node.key:
			node.left = self.delete_node(node.left,key)
		elif node.left and node.right:
			temp = self.findmax(node.left)
			node.key = temp.key
			node.left = self.delete_node(node.left,node.key)
		else:
			if node.left is None:
				node = node.right
			else:
				node = node.left
				self.size -= 1
		return node
			
	def findmax(self,node):
		if node is not None:
			self.findmax(node.right)
		return node


	def inorder_traversal(self,node):
		if node is not None:
			self.inorder_traversal(node.left)
			print(node.key)
			self.inorder_traversal(node.right)

	def preorder_traversal(self,node):
		if node is not None:
			print(node.key)
			self.preorder_traversal(node.left)
			self.preorder_traversal(node.right)

	def postorder_traversal(self,node):
		if node is not None:
			self.postorder_traversal(node.left)
			self.postorder_traversal(node.right)
			print(node.key)

	def levelorder_traversal(self):
		q = ArrayQueue.ArrayQueue()
		node = self.root
		q.enqueue(node)
		while q.len() != 0:
			node = q.dequeue()
			print(node.key)
			if node.left is not None:
				q.enqueue(node.left)
			if node.right is not None:
				q.enqueue(node.right)




	def search(self,key):
		flag = False
		cur = self.root
		while cur is not None:
			if key > cur.key:
				cur = cur.right
			elif key < cur.key:
				cur = cur.left
			else:
				break	
		return cur != None

	def searchfor(self,key):
		value = self.search(key)
		if value:
			print("key found")
		else:
			print("not found")

		

def main():
	tree = BinarySearchTree()
	tree.insert(44,4)
	tree.insert(33,4)
	tree.insert(55,4)
	#tree.inorder_traversal(tree.root)
	#tree.preorder_traversal(tree.root)
	#tree.postorder_traversal(tree.root)
	#tree.delete(44)
	tree.insert(40,6)
	tree.insert(22,5)
	tree.insert(66,7)
	tree.levelorder_traversal()
	#tree.searchfor(66)
	

main()


	