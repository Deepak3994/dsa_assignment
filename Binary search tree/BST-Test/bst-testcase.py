from BST import bst

def test_empty_bst():
	tree = bst.BST()
	assert(tree.bst_len() == 0)

def test_bst():
	tree = bst.BST()
	assert(tree.bst_len() == 0)
	tree.bst_add(30)
	tree.bst_add(20)
	tree.bst_add(40)
	tree.bst_add(50)
	assert(tree.bst_len() == 4)
	assert(tree.bst_search(20) == 1)
	assert(tree.bst_search(40) == 1)
	assert(tree.bst_search(30) == 1)
	assert(tree.bst_search(10) == 0)
	#tree.bst_inorder()
	tree.bst_delete(50)
	assert(tree.bst_len() == 3)
	tree.bst_delete(30)
	assert(tree.bst_len() == 2)
	tree.bst_delete(90)
	#tree.bst_inorder()
	assert(tree.bst_search(30) == 0)

	tree.bst_delete(20)
	tree.bst_delete(40)
	assert(tree.bst_len() == 0)
	print(tree.isempty())

	tree.bst_add(50)
	tree.bst_add(60)
	assert(tree.bst_len() == 2)
	tree.bst_inorder()

test_empty_bst()
test_bst()
