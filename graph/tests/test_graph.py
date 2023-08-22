from graph.graph import Graph, Vertex, Edge, Queue

def test_add_vertex_to_graph():
    graph = Graph()
    vertex = graph.add_vertex('A')
    assert vertex.value == 'A'
    assert vertex in graph.get_vertices()

def test_add_edge_to_graph():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    graph.add_edge(vertex_a, vertex_b, weight=5)

    neighbors_a = graph.get_neighbors(vertex_a)
    neighbors_b = graph.get_neighbors(vertex_b)

    assert len(neighbors_a) == 1
    assert len(neighbors_b) == 1

    edge_ab = neighbors_a[0]
    edge_ba = neighbors_b[0]

    assert edge_ab.vertex == vertex_b
    assert edge_ab.weight == 5
    assert edge_ba.vertex == vertex_a
    assert edge_ba.weight == 5

def test_get_all_vertices():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')

    vertices = graph.get_vertices()

    assert vertex_a in vertices
    assert vertex_b in vertices
    assert vertex_c in vertices

def test_get_neighbors():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')
    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_a, vertex_c)
    
    neighbors_a = graph.get_neighbors(vertex_a)
    neighbors_b = graph.get_neighbors(vertex_b)
    neighbors_c = graph.get_neighbors(vertex_c)
    
    assert len(neighbors_a) == 2
    assert len(neighbors_b) == 1
    assert len(neighbors_c) == 1
    
    neighbor_values_a = [edge.vertex.value for edge in neighbors_a]
    assert 'B' in neighbor_values_a
    assert 'C' in neighbor_values_a
    
    neighbor_values_b = [edge.vertex.value for edge in neighbors_b]
    assert 'A' in neighbor_values_b
    
    neighbor_values_c = [edge.vertex.value for edge in neighbors_c]
    assert 'A' in neighbor_values_c

def test_get_neighbors_with_weight():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    graph.add_edge(vertex_a, vertex_b, weight=5)
    
    neighbors_a = graph.get_neighbors(vertex_a)
    neighbors_b = graph.get_neighbors(vertex_b)
    
    edge_ab = neighbors_a[0]
    edge_ba = neighbors_b[0]
    
    assert edge_ab.weight == 5
    assert edge_ba.weight == 5

def test_graph_size():
    graph = Graph()
    assert graph.size() == 0
    
    vertex_a = graph.add_vertex('A')
    assert graph.size() == 1
    
    vertex_b = graph.add_vertex('B')
    assert graph.size() == 2
    
    graph.add_edge(vertex_a, vertex_b)
    assert graph.size() == 2  

def test_single_vertex_and_edge_graph():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    graph.add_edge(vertex_a, vertex_a, weight=3)
    
    neighbors_a = graph.get_neighbors(vertex_a)
    
    assert len(neighbors_a) == 1
    assert neighbors_a[0].vertex == vertex_a
    assert neighbors_a[0].weight == 3

