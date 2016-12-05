class BST:
	class _Node:
		def __init__(self, k):
			self._key = k
			self._left = None
			self._right = None

	def __init__(self):
		self._root = None
		self._mass = 0

	def isempty(self):
		return self._mass == 0

	def bst_add(self, ele):
		root = parent = self._root
		while root is not None and root._key is not ele:
			parent = root
			if ele < root._key:
				root = root._left
			else:
				root = root._right

		if root is None:
			new_node = self._Node(ele)
			if parent is None:
				self._root = new_node
			elif ele < parent._key:
				parent._left = new_node
			else:
				parent._right = new_node
			self._mass += 1

	def bst_search(self, key):
		node = self._root
		while node is not None:
			if key < node._key:
				node = node._left
			elif key > node._key:
				node = node._right
			else:
				break
		return node != None

	def bst_len(self):
		return self._mass


	def bst_inorder(self):
		if not self.isempty():
			root = self._root
			self.__inorder(root)

	def __inorder(self, root):
		if not root is None:
			self.__inorder(root._left)
			print(root._key)
			self.__inorder(root._right)

	def bst_delete(self, ele):
		if not self.isempty():
			root = self._root
			self.__delete(root, ele)
			if self.isempty():
				self._root = None


	def __delete(self, root, ele):
		if root is None:
			return
		if ele < root._key:
			root._left = self.__delete(root._left, ele)
		elif ele > root._key:
			root._right = self.__delete(root._right, ele)
		#elif root._left is not None and root._right is not None:
		elif root._left  and root._right:
			temp = self.__findMax(root._right)
			root._key = temp._key
			root._right = self.__delete(root._right, root._key)
		else:
			if root._left is None:
				root = root._right
			else:
				root = root._left
			self._mass -= 1
		return root

	def __findMax(self, root):
		if root._left is None:
			return root
		else:
			return self._findMax(root._left)
