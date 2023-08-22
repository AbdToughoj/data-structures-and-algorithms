from graph_depth_first.graph_depth_first import Graph

graph = Graph()
a = graph.add_vertex('A')
b = graph.add_vertex('B')
c = graph.add_vertex('C')
d = graph.add_vertex('D')
e = graph.add_vertex('E')
f = graph.add_vertex('F')
h = graph.add_vertex('H')
g = graph.add_vertex('G')

graph.add_edge(a, b)
graph.add_edge(b, a)
graph.add_edge(b, c)
graph.add_edge(c, b)
graph.add_edge(d, a)
graph.add_edge(d, b)
graph.add_edge(d, e)
graph.add_edge(d, h)
graph.add_edge(d, f)
graph.add_edge(e, d)
graph.add_edge(f, h)
graph.add_edge(f, d)
graph.add_edge(h, f)
graph.add_edge(h, d)
graph.add_edge(c, g)
graph.add_edge(g, c)


def test_depth_first():
    start_node = 'A'
    dfs_result = graph.depth_first(start_node)
    actual = ", ".join(dfs_result)
    expected = "A, B, C, G, D, E, H, F"

    assert actual == expected

def test_depth_first_start_at_d():
    start_node = 'D'
    dfs_result = graph.depth_first(start_node)
    actual = ", ".join(dfs_result)
    expected = "D, A, B, C, G, E, H, F"

    assert actual == expected

def test_depth_first_empty_graph():
    graph = Graph()

    start_node = 'A' 
    dfs_result = graph.depth_first(start_node)
    actual = ", ".join(dfs_result)
    expected = ""

    assert actual == expected