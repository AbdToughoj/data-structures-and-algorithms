class Node:
    def __init__(self, value):
        """
        Initializes a new node with the given value.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Initializes a new empty linked list.
        """
        self.head = None

    def insert(self, value):
        """
        Inserts a new node with the given value at the head of the linked list.

        Args:
            value: The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def includes(self, value):
        """
        Checks if a node with the given value exists in the linked list.

        Args:
            value: The value to search for.

        Returns:
            True if the value is found, False otherwise.
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        """
        Generates a string representation of the linked list.

        Returns:
            A string representing the values in the linked list, formatted as:
            "{ a } -> { b } -> { c } -> NONE"
        """
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values) + ' -> NONE'

    def append(self, value):
        """
        Adds a new node with the given value to the end of the list.

        Args:
            value: The value to be appended.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_before(self, value, new_value):
        """
        Adds a new node with the given new value immediately before the first node that has the value specified.

        Args:
            value: The value to search for.
            new_value: The new value to be inserted.
        """
        new_node = Node(new_value)
        if self.head is None:
            return

        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def insert_after(self, value, new_value):
        """
        Adds a new node with the given new value immediately after the first node that has the value specified.

        Args:
            value: The value to search for.
            new_value: The new value to be inserted.
        """
        new_node = Node(new_value)
        if self.head is None:
            return

        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next


