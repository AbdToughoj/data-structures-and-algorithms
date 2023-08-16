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
    
def depth_first():
    pass
