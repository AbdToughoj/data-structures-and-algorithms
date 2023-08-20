'''
- implement the graph with all methods needed.
- vertex  *
- Edge  *
- graph *
methods : 
  - add_vertex() * 
  - add_edge() *
  - get_vertices() *
  - get_neighbors() *
  - size () *
- breadth first traversal . 
  - Queue() *
'''
from collections import deque 

class Queue:

    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)



class Vertex:
    '''
    Represents a vertex in the graph.
    '''

    def __init__(self, value):

        self.value = value

    def __str__(self):
        return self.value


class Edge:
    '''
    Represents an edge between two vertices in the graph.
    '''
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex

class Graph:
    '''
    Represents a graph and its operations.
    '''

    def __init__(self):
        self.__adj_list = {}

    def add_vertex(self,value):
      '''
      Arguments: value
      Returns: The added vertex
      Add a vertex to the graph
      '''

      vertex = Vertex(value)
      self.__adj_list[vertex] = []
      return vertex



    def add_edge(self, start_vertex, end_vertex, weight=0):
        '''
        Arguments: 2 vertices to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
        '''
        if start_vertex not in self.__adj_list:
            raise KeyError("Vertex does not exist")
        if end_vertex not in self.__adj_list:
            raise KeyError("Vertex does not exist")
        if start_vertex == end_vertex:
            edge1 = Edge(end_vertex, weight)
            self.__adj_list[start_vertex].append(edge1)
            return
        edge1 = Edge(end_vertex, weight)
        edge2 = Edge(start_vertex,weight)
        self.__adj_list[start_vertex].append(edge1)
        self.__adj_list[end_vertex].append(edge2)



    def get_vertices(self):
      '''
      Arguments: none
      Returns all of the vertices in the graph as a collection (set, list, or similar)
      Empty collection returned if there are no vertices
      '''

      return self.__adj_list.keys()


    def size(self):
        '''
        Returns the number of vertices in the graph.
        '''
        return len(self.__adj_list)

    def get_neighbors(self,vertex):
      '''
      get neighbors
      Arguments: vertex
      Returns a collection of edges connected to the given vertex
      Include the weight of the connection in the returned collection
      Empty collection returned if there are no vertices
      '''
      return self.__adj_list.get(vertex, [])


    def breadth_first(self,start_vertex):
        '''
        Performs breadth-first traversal of the graph starting from the given vertex.
        Arguments:
        - start_vertex: The starting vertex for traversal
        Returns:
        List of vertices in breadth-first order
        '''
        q = Queue()
        result = []
        visited = set()

        q.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(q):
            current_vertex = q.dequeue()

            result.append(current_vertex.value)

            neighbors =self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.add(neighbor)

        return result

    def depth_first(self, start_vertex):
        '''
        Performs depth-first traversal of the graph starting from the given vertex.
        Arguments:
        - start_vertex: The starting vertex for traversal
        Returns:
        List of vertices in pre-order depth-first order
        '''
        def dfs_recursive(vertex, visited, result):
            visited.add(vertex)
            result.append(vertex.value)
            neighbors = self.get_neighbors(vertex)
            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    dfs_recursive(neighbor, visited, result)

        result = []
        visited = set()
        start_vertex = Vertex(start_vertex)
        dfs_recursive(start_vertex, visited, result)
        return result
