class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, end_vertex, weight=0):
        self.end_vertex = end_vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.__adj_list = {}
      
    def add_vertex(self, value):
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adj_list:
            raise KeyError(f"Start vertex {start_vertex} is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError(f"End vertex {end_vertex} is not found")
        edge1 = Edge(end_vertex, weight)
        self.__adj_list[start_vertex].append(edge1)
        if start_vertex != end_vertex:
            edge2 = Edge(start_vertex, weight)
            self.__adj_list[end_vertex].append(edge2)

    def get_vertices(self):
        return list(self.__adj_list.keys())

    def size(self):
        return len(self.__adj_list)
  
    def get_neighbors(self, vertex):
        return self.__adj_list.get(vertex, [])
    

def graph_business_trip(graph, start_vertex, end_vertex):
    if start_vertex not in graph.get_vertices():
        raise KeyError(f"Start vertex {start_vertex} is not found")
    if end_vertex not in graph.get_vertices():
        raise KeyError(f"End vertex {end_vertex} is not found")
    if start_vertex == end_vertex:
        raise ValueError(f"Start and end vertices cannot be the same")
    path = []
    path.append(start_vertex)
    current_vertex = start_vertex
    while current_vertex!= end_vertex:
        for edge in graph.get_neighbors(current_vertex):
            if edge.end_vertex == end_vertex:
                path.append(edge.end_vertex)
                current_vertex = edge.end_vertex
                break
        else:
            raise ValueError(f"No path found between {start_vertex} and {end_vertex}")
    return path