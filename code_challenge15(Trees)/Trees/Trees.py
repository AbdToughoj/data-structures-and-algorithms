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

    def pre_order(self):
        """
        Performs pre-order traversal on the binary tree.
        
        Returns:
            A list containing the values of the nodes in pre-order traversal order.
        """
        if self.root is None:
            return None
        else:
            output = []

            def _helper(root):
                output.append(root.value)
                if root.left:
                    _helper(root.left)
                if root.right:
                    _helper(root.right)

            _helper(self.root)
            return output

    def in_order(self):
        """
        Performs in-order traversal on the binary tree.

        Returns:
            A list containing the values of the nodes in in-order traversal order.
        """
        if self.root is None:
            return None
        else:
            output = []

            def _helper(root):
                if root.left:
                    _helper(root.left)
                output.append(root.value)
                if root.right:
                    _helper(root.right)

            _helper(self.root)
            return output

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
