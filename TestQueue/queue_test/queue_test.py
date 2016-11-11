
from queues import Array_queue

def test_empty_queue():
	q = Array_queue.ArrayQueue()
	assert(q.len() == 0)
	q.dequeue()

def test_one_element_queue():
	q = Array_queue.ArrayQueue()
	q.enqueue(10)
	assert (q.len() == 1)
	q.dequeue()
	assert(q.is_empty())

def test_queue_growth():
	q = Array_queue.ArrayQueue()
	assert (q.capacity() == 2)
	q.enqueue(10)
	q.enqueue(20)
	assert(q.len() == 2)
	assert(q.capacity() == 2)
	q.enqueue(30)
	assert (q.capacity() == 4)

def test_queue_shrink():
	q = Array_queue.ArrayQueue()
	assert (q.capacity() == 2)

	for ele in range(8):				# let queue grow
		q.enqueue(ele)
	assert (q.capacity() == 8)

	for ele in range(6):
		q.dequeue()

	assert (q.capacity() == 8)
	print (q.len())



if __name__ == '__main__':
	#test_empty_queue()
	#test_one_element_queue()
	test_queue_shrink()

