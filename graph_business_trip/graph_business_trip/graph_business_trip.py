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
    
def business_trip(graph, city_names):
    """
    Calculates the total cost of a business trip based on a route map graph and a list of city names.
    
    Arguments:
    - graph: An instance of the Graph class representing the route map.
    - city_names: A list of strings containing the names of cities in the desired order of the trip.
    
    Returns:
    - The total cost of the trip if it's possible with direct flights between consecutive cities,
      or "null" if the trip is not possible or the input is insufficient.
    """
    total_cost = 0
    
    vertices = graph.get_vertices() 
    
    for i in range(len(city_names) - 1):
        current_city_name = city_names[i]
        next_city_name = city_names[i + 1]
        
        current_city_vertex = None
        next_city_vertex = None
        for vertex in vertices:
            if vertex.value == current_city_name:
                current_city_vertex = vertex
            if vertex.value == next_city_name:
                next_city_vertex = vertex
        
        if current_city_vertex is None or next_city_vertex is None:
            return "null"
        
        neighbors = graph.get_neighbors(current_city_vertex)
        
        found = False
        
        for edge in neighbors:
            if edge.vertex.value == next_city_name:
                total_cost += edge.weight
                found = True
                break
        
        if not found:
            return "null"
    
    return total_cost




    
if  __name__ == "__main__":
    route_map = Graph()

    pandora = route_map.add_vertex("Pandora")
    arendelle = route_map.add_vertex("Arendelle")
    metroville = route_map.add_vertex("Metroville")
    monstropolis = route_map.add_vertex("Monstropolis")
    naboo = route_map.add_vertex("Naboo")
    narnia = route_map.add_vertex("Narnia")

    route_map.add_edge(pandora, arendelle, 150)
    route_map.add_edge(arendelle, metroville, 99)
    route_map.add_edge(metroville, monstropolis, 105)
    route_map.add_edge(monstropolis, arendelle, 42) 
    route_map.add_edge(metroville, pandora, 82)
    route_map.add_edge(metroville, monstropolis, 105)
    route_map.add_edge(metroville, naboo, 26)
    route_map.add_edge(metroville, narnia, 37)
    route_map.add_edge(monstropolis, naboo, 73)
    route_map.add_edge(naboo, metroville, 26)
    route_map.add_edge(naboo, narnia, 250)
    route_map.add_edge(narnia, metroville, 37)
    route_map.add_edge(narnia, naboo, 250)

    print(business_trip(route_map, ["Metroville", "Pandora"]))  # Output: 82
    print(business_trip(route_map, ["Arendelle", "Monstropolis", "Naboo"]))  # Output: 115
    print(business_trip(route_map, ["Naboo", "Pandora"]))  # Output: null
    print(business_trip(route_map, ["Narnia", "Arendelle", "Naboo"]))  # Output: null



