class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def find_maximum_value(self):
        if self.root is None:
            raise ValueError("Tree is empty.")

        return self._find_maximum_value_helper(self.root)