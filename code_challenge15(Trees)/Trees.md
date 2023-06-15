# Challenge Title

Node:

- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
  Binary Tree:
- Create a Binary Tree class
  _ Define a method for each of the depth first traversals:
  _ pre order
  _ in order
  _ post order Each depth first traversal method should return an array of values, ordered appropriately.
  Binary Search Tree:
- Create a Binary Search Tree class
  - This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
  - Add
    - Arguments: value
    - Return: nothing
    - Adds a new node with that value in the correct location in the binary search tree.
  - Contains
    - Argument: value
    - Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

#### **Approach:**

The code consists of two classes, Tnode and Tree, representing nodes and a binary tree, respectively. The Tnode class initializes a node with a value and attributes for left and right child nodes. The Tree class initializes a binary tree and provides traversal methods (pre_order, in_order, and post_order) for different traversal orders. The Binary_search class extends Tree to represent a binary search tree, with additional methods for insertion (add) and checking if a value exists (contains). The code allows for working with binary trees and binary search trees, including traversal and insertion operations.

#### **Big O:**

- Space Complexity: O(n)
- Time Complexity: O(n)

## Solution

![Solution](<../code_challenge15(Trees)/assets/Trees_Run.png>)
