# Challenge Title

Implement a Graph. The graph should be represented as an adjacency list, and should include the following methods:

- add vertex

  - Arguments: value
  - Returns: The added vertex
  - Add a vertex to the graph

- add edge

  - Arguments: 2 vertices to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two vertices in the graph
  - If specified, assign a weight to the edge
  - Both vertices should already be in the Graph

- get vertices

  - Arguments: none
  - Returns all of the vertices in the graph as a collection (set, list, or similar)
  - Empty collection returned if there are no vertices

- get neighbors

  - Arguments: vertex
  - Returns a collection of edges connected to the given vertex
    - Include the weight of the connection in the returned collection
  - Empty collection returned if there are no vertices

- size
  - Arguments: none
  - Returns the total number of vertices in the graph
  - 0 if there are none

## Approach & Efficiency

### Approach:

The provided code implements a graph data structure with vertex and edge representations. It includes methods for adding vertices and edges, retrieving vertices and neighbors, calculating the size of the graph, and performing breadth-first traversal. The graph is represented using an adjacency list. The Graph class utilizes the Vertex and Edge classes to create a structure for representing vertices and edges. The Graph class methods allow for adding vertices and edges, retrieving vertices and neighbors, calculating the graph's size, and performing breadth-first traversal using a queue. The implementation follows the graph data structure's fundamental principles, enabling manipulation and analysis of graphs in terms of vertices and edges.

### Big O:

- Space Complexity:
  - breadth_first : O(V)
- Time Complexity:
  - breadth_first : O(V + E)

## Solution

Use pytest to run the tests in the test_graph.py file to make sure of the solution.
