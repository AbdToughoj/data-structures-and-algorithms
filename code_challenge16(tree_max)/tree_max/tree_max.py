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
        
    def max_tree(self):
        """
        Finds the maximum value in the binary tree.

        Returns:
            The maximum value found in the tree.
            If the tree is empty, returns "no max: the tree is empty".
        """
        if self.root is None:
            return "No max: the tree is empty"
        else:
            output = []

            def _helper(root):
                if root.left:
                    _helper(root.left)
                output.append(root.value)
                if root.right:
                    _helper(root.right)

            _helper(self.root)
            max_tnode = output[0]
            for x in output:
                if x > max_tnode:
                    max_tnode = x
            return max_tnode
