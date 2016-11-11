from QueueLinked import Linked_Queue	
	

def test_empty_queue():
	s = Linked_Queue.LinkedQueue()
	assert (s.len() == 0)
	

def test_one_element_queue():
	s = Linked_Queue.LinkedQueue()
	s.enqueue(10)
	assert (s.len() == 1)	
	assert (s.first() == 10)
	s.dequeue()
	assert (s.is_empty())


def test_multi_element_queue():
	s = Linked_Queue.LinkedQueue()
	for e in range(10):
		s.enqueue(e)

	assert(s.len() == 10)
	for e in range(10):
		s.dequeue()
	
	assert (s.len() == 0)
	


if __name__ == '__main__':
	test_empty_queue()
	test_one_element_queue()
	test_multi_element_queue()
	
