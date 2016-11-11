from SLL import single_list

def test_empty_list():
	s = single_list.SingleList()
	assert (s.len() == 0)
	

def test_one_node_list():
	s = single_list.SingleList()
	s.add_first(10)
	assert (s.len() == 1)	
	assert (s.first() == 10)


def test_multi_element_list():
	s = single_list.SingleList()
	for e in range(10):
		s.add_first(e)

	assert (s.lookup(5))
	assert(s.len() == 10)
	s.delete_first()
	assert (s.len() == 9)
	assert (s.first() == 8)

def test_add_tail():
	s = single_list.SingleList()
	s.add_last(10)
	

if __name__ == '__main__':
	test_empty_list()
	test_one_node_list()
	test_multi_element_list()
	test_add_tail()
