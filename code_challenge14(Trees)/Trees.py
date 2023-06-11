class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def preorder_traversal(self, node, traversal):
        if node:
            traversal.append(node.value)
            traversal = self.preorder_traversal(node.left, traversal)
            traversal = self.preorder_traversal(node.right, traversal)
        return traversal
    
    def inorder_traversal(self, node, traversal):
        if node:
            traversal = self.inorder_traversal(node.left, traversal)
            traversal.append(node.value)
            traversal = self.inorder_traversal(node.right, traversal)
        return traversal
    
    def postorder_traversal(self, node, traversal):
        if node:
            traversal = self.postorder_traversal(node.left, traversal)
            traversal = self.postorder_traversal(node.right, traversal)
            traversal.append(node.value)
        return traversal