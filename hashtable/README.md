# Challenge Title

Implement a Hashtable Class with the following methods:

- set
  - Arguments: key, value
  - Returns: nothing
  - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  - Should a given key already exist, replace its value from the value argument given to this method.
- get
  - Arguments: key
  - Returns: Value associated with that key in the table
- has
  - Arguments: key
  - Returns: Boolean, indicating if the key exists in the table already.
- keys
  - Returns: Collection of keys
- hash
  - Arguments: key
  - Returns: Index in the collection for that key

## Approach & Efficiency

### Approach:

The code defines three classes: Node, LinkedList, and HashTable.

The Node class represents a node in a linked list or other data structures and has two main components: the value of the node and a reference to the next node.

The LinkedList class represents a singly linked list data structure, where each node is connected to the next node through the next reference. The insert method adds a new node with the given value at the beginning of the linked list.

The HashTable class represents a data structure that stores key-value pairs of data using buckets to increase data accessing efficiency. It uses a hash function, **hash, to generate a hash code for each key, which is then used to determine the index where the key-value pair will be stored in the internal list called **buckets. The set method stores the key-value pair in the appropriate bucket, handling collisions by using separate linked lists for each bucket. The get method retrieves the value associated with the given key from the hashtable. The has method checks if the given key exists in the hashtable, and the get_keys method returns a list of all the keys present in the hashtable. The hash function uses the reduce function to calculate the hash code from the ASCII values of the characters in the key.

### Big O:

- Space Complexity: O(n)
  - Node: O(1)
  - LinkedList: O(n)
  - HashTable: O(n)
- Time Complexity: O(n)
  - \_\_hash: O(n)
  - set: O(n)
  - get: O(n)

## Solution

This solution defines three classes: Node, LinkedList, and HashTable. The Node class represents a node in a linked list, the LinkedList class represents a singly linked list data structure, and the HashTable class represents a data structure that stores key-value pairs using buckets to increase data accessing efficiency.

The hash function (\_\_hash) calculates the hash code for the given key, and the set method sets a key-value pair in the hashtable, handling collisions using separate linked lists for each bucket. The get method retrieves the value associated with the given key from the hashtable. The has method checks if a given key exists in the hashtable. The get_keys method returns a list of all the keys present in the hashtable.

Note: Use pytest to run the tests in the hashtable_test.py file to make sure of the solution.
