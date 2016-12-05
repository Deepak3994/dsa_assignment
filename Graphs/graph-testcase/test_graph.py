from graph import graph


def test_empty_graph():
	g = graph.Graph()
	assert(g.get_vertex_count() == 0)

def test_three_node_graph():
	g = graph.Graph()
	g.add_vertex('a')
	g.add_vertex('b')
	g.add_vertex('c')

	g.add_edge('a', 'b', '10')
	g.add_edge('a', 'c', '5')
	assert(g.get_vertex_count() == 3)
	assert(g.get_adjacent('a') == ['b','c'])
	assert(g.get_adjacent('b') == ['a'])
	assert(g.get_adjacent('c') == ['a'])
	

def test_graph():
	g = graph.Graph()
	g.add_vertex('a')
	g.add_vertex('b')
	g.add_vertex('c')
	g.add_vertex('d')
	g.add_vertex('e')

	g.add_edge('a', 'b', 10)
	g.add_edge('a', 'c', 5)
	g.add_edge('b', 'c', 15)
	g.add_edge('c', 'd', 4)
	g.add_edge('b', 'e', 20)
	assert(g.get_vertex_count()== 5)
	assert(g.get_edge_cost('a', 'b') == 10)
	assert(g.get_edge_cost('b', 'e') == 20)
	
	

def test_path():
	g = graph.Graph()
	g.add_vertex('a')
	g.add_vertex('b')
	g.add_vertex('c')
	g.add_vertex('d')
	g.add_vertex('e')

	g.add_edge('a', 'b', 10)
	g.add_edge('a', 'c', 5)
	g.add_edge('b', 'c', 15)
	g.add_edge('c', 'd', 4)
	g.add_edge('b', 'e', 20)

	print(g.find_path('a', 'd'))
	

def test_all_paths():
	g = graph.Graph()
	g.add_vertex('a')
	g.add_vertex('b')
	g.add_vertex('c')
	g.add_vertex('d')
	g.add_vertex('e')

	g.add_edge('a', 'b', 10)
	g.add_edge('a', 'c', 5)
	g.add_edge('b', 'c', 15)
	g.add_edge('c', 'd', 4)
	g.add_edge('b', 'e', 20)
	print(g.find_all_paths('a', 'b'))

def test_costs():
	g = graph.Graph()
	g.add_vertex('a')
	g.add_vertex('b')
	g.add_vertex('c')
	g.add_vertex('d')
	g.add_vertex('e')

	g.add_edge('a','b', 10)
	g.add_edge('a', 'c', 5)
	g.add_edge('c', 'd', 21)
	g.add_edge('b', 'e', 32)
	g.add_edge('d', 'b', 10)
	d1= { 'a':20,'b':10,'c':21, 'd':0, 'e':42  }
	assert(g.shortest_path('d') == d1)

test_empty_graph()
test_three_node_graph()
test_graph()
test_path()
test_all_paths()
test_costs()
