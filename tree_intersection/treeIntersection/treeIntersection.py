from functools import reduce
from operator import add

class Tnode:
    def __init__(self, value):
        """
        Initializes a new instance of the Tnode class.

        Args:
            value: The value to be assigned to the node.
        """
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        """
        Initializes a new instance of the Tree class.
        """
        self.root = None

    def post_order(self):
        """
        Performs post-order traversal on the binary tree.

        Returns:
            A list containing the values of the nodes in post-order traversal order.
        """
        if self.root is None:
            return None
        else:
            output = []

            def _helper(root):
                if root.left:
                    _helper(root.left)
                if root.right:
                    _helper(root.right)
                output.append(root.value)

            _helper(self.root)
            return output

class Binary_search(Tree):

    def add(self, value):
        """
        Adds a new node with the specified value to the binary search tree.

        Args:
            value: The value to be added to the tree.
        """
        if self.root is None:
            self.root = Tnode(value)
        else:
            self.add_node(self.root, value)

    def add_node(self, current, value):
        """
        Helper method to recursively add a new node to the binary search tree.

        Args:
            current: The current node being examined during the traversal.
            value: The value to be added to the tree.
        """
        if value < current.value:
            if current.left is None:
                current.left = Tnode(value)
            else:
                self.add_node(current.left, value)
        else:
            if current.right is None:
                current.right = Tnode(value)
            else:
                self.add_node(current.right, value)

    def contains(self, value):
        """
        Checks if the binary search tree contains a node with the specified value.

        Args:
            value: The value to be searched in the tree.

        Returns:
            True if the value is found, False otherwise.
        """
        if self.pre_order() is None:
            return 'The tree is empty'
        elif value in self.pre_order():
            return True
        else:
            return False
        

class Node:
  '''
  A class represent a node in a linked list or other data structure each node has two main componenet the value of the node and the reference to the next node.
  args: value
  return : nothing
  '''
  def __init__(self, value):
      self.next=None 
      self.value=value



class LinkedList:
  '''
  what : A class representing a singly linked list data structure
  '''
  def __init__(self):
    self.head = None


  def insert (self, value):
    '''
    insert a new node with the given value at the begining of     the linked list.
    args: value
    output : none
    
    '''
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node


class HashTable:
  '''
  what : data structure that store key-value pairs of data using buckets to increace data accessing efficiency 
  
  '''
  def __init__(self,size=1024):
    self.__size=size
    self.__buckets=[None] *size
    self.keys = []
    
  
  def __hash(self,key):
    '''
    A method to return the hash code of the given key
    arg : key
    output: hash code of the key(index)
    '''
    # code = 0
   
    # for char in key:
    #   code += ord(str(char)) # * weight
    # code *= 255
    # code = code % 1024
    # return code
    return reduce(add, [ord(str(char)) for char in str(key)]) * 283 % self.__size
    return sum([ord(str(char)) for char in key]) * 283 % self.__size

  
    
  def set(self,key,value):
    '''
    Set a key-value pair in the bucket, handling collisions as              needed.
    Arguments:
    key : The key to be hashed and used as the identifier for the           value.
    value : the value that is aassociated with the key
    Returns: None
    '''
    index = self.__hash(key)
    if self.__buckets[index] is None:
      ll = LinkedList()
      self.__buckets[index] = ll
     
    self.__buckets[index].insert([key,value])
    self.keys.append(key)
    
    

 

  def get(self,key):
    '''
    Retrieve the value with the given key from the hashtable
    arg : key
    return : value or None 
    '''
    index=self.__hash(key)
    bucket = self.__buckets[index]
    if bucket is not None : 
      curr = bucket.head
      while curr :
        if curr.value[0] == key :
          return curr.value[1]
        curr = curr.next  
    return None  
    
    

  def has(self, key):
    '''
    A method to check if the given key exist in the hashtable.
    arg: key
    output: boolean
    ''' 
    if self.get(key):
      return True
    return False  

    

  def get_keys(self):
    '''
    args : none
    Returns a list of all the  keys present in the Hashtable.
    '''
    return self.keys
        
def treeIntersection(tree1,tree2):
    '''
    args : two binary search tree
    return : list of common values
    '''
    hashtable = HashTable()
    commonVal= []
    for i in tree1.post_order():
       hashtable.set(i,i)
    for i in tree2.post_order():
        if hashtable.has(i):
            commonVal.append(i)
    return commonVal




        
if __name__ == "__main__":


    tree1 = Binary_search()
    tree1.add(3)
    tree1.add(1)
    tree1.add(5)
    tree1.add(2)
    tree1.add(4)

    tree2 = Binary_search()
    tree2.add(5)
    tree2.add(2)
    tree2.add(7)
    tree2.add(6)
    tree2.add(8)


    print(treeIntersection(tree1, tree2))


