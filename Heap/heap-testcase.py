from Heap import heap

def test_empty_heap():
	h = heap.Heap()
	assert(h.is_empty())	

def test_two_element_heap():
	h = heap.Heap([10,5])
	h.test_heap_order()	
	assert(h.remove_min() == 5)
	assert(h.min() == 10)	

def test_build_heap():
	h = heap.Heap()
	h.add(10)
	h.add(30)
	h.add(90)
	h.add(60)
	h.add(0)
	assert(h.__len__() == 5)
	h.test_heap_order()
	assert(h.min() == 0)

def test_sorting():
	h = heap.Heap([20,10,4,90,60,57,250])
	h.heap_sort()
	

test_empty_heap()
test_two_element_heap()
test_build_heap()
test_sorting()