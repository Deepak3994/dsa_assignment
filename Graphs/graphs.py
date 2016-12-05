class graph:

	class vertex:

		def __init__(self,node):
			self.vertex_id = node
			self.adjacent = {}
		
		def neighbour_present(self,node):
			return node in self.adjacent
		
		def add_neighbour(self,node,weight=0):
			if not self.neighbour_present(node):
				self.adjacent[node] = weight
		
		def get_neighbours(self):
			return self.adjacent.keys()
		
		def get_weight(self,node):
			if self.neighbour_present(node):
				return self.adjacent[node]
			else:
				return sys.maxsize
	
	def __init__(self):
		self.vertex_count = 0
		self.adjacency_list = {}
	
	def is_empty(self):
		return self.vertex_count == 0
	
	def vertex_present(self,node):
		return node in self.adjacency_list
	
	def add_vertex(self,node):
		if not self.vertex_present(node):
			self.vertex_count += 1
			new_vertex = vertex(node)
			self.adjacency_list[node] = new_vertex
	
	def add_edge(self,frm,to,cost=0):
		if not self.vertex_present(frm):
			self.add_vertex(frm)
	    if not self.vertex_present(to):
			self.add_vertex(to)
		self.adjacency_list[frm].add_neighbour(to,cost)
		#if it is a direxted graph stop here else continue
		self.adjacency_list[to].add_neighbour(frm,cost)

	def get_neighbours(self,node):
		if self.vertex_present(node):
			return self.adjacency_list[node].get_neighbours()

	def find_path(self,start,end,path = []):
		path = path + [start]
		if start == end:
			return path
		if not start in self.adjacency_list:
			return None
		neighbour_lst = self.get_neighbours(start)
		for node in neighbour_lst:
			if node in  not path:
				new_path = self.find_path(node,end,path)
				if new_path : return new_path
		return None

	def find_all_path(self,start,end,path = []):
		path = path + [start]
		if start == end:
			return path
		if not start in self.adjacency_list:
			return None
		paths = []
		neighbour_lst = self.get_neighbours(start)
		for node in neighbour_lst:
			if node in  not path:
				new_paths = self.find_all_path(node,end,path)
				for new_path in new_paths:
					paths.append(new_path)
		return paths

	def shortest_path(self,start):
		visited = {}
		distance = {}
		neighbour_lst = self.adjacency_list.keys()
		for node in neighbour_lst:
			visited[node] = False
			distance[node] = self.adjacency_list[start].get_weight(node)
		visited[start] = True
		distance[start] = 0
		for node in neighbour_lst:
			vertex = self.choose_nearest_vertex(visited,distance)
			visited[vertex] = True
			for dest in neighbour_lst:
				new_distance = distance[vertex] + self.adjacency_list[vertex].get_weight(dest)
				if new_distance < distance[dest]:
					distance[dest] = new_distance
		return distance

	def choose_nearest_vertex(self,visited,distance):
		neighbour_lst = self.adjacency_list.keys()
		minimum = sys.maxsize
		nearest = None
		for node in neighbour_lst:
			if distance[node] < minimum and not visited[node]:
				minimum = distance[node]
				nearest = node
		return nearest


    #test cases
    def empty_graph():
	    g = graph
	    assert(g.get_weight()==0)

	def test_three_node_graph():
		g = graph
		g.add_vertex(a)
		g.add_vertex(b)
		g.add_vertex(c)
		g.add_edge('a','b',10)
		g.add_edge('a','c',5)
		assert(g.get_weight()==3)
		print(g.get_neighbours('a'))

	def test_four_node_graph():
		g = graph
		g.add_vertex(a)
		g.add_vertex(b)
		g.add_vertex(c)
		g.add_vertex(d)
		g.add_vertex(e)
		g.add_edge('a','b',10)
		g.add_edge('a','c',5)
		g.add_edge('b','',15)
		g.add_edge('c','d',4)
		g.add_edge('d','e',20)
		print(g.get_neighbours('a','d'))
		print(g.shortest_path('d'))
