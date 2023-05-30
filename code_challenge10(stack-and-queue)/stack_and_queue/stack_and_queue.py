class Node:
    def __init__(self, value):
        """
        Initializes a new Node object with the given value.

        Args:
            value: The value to be stored in the Node.
        """
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        """
        Initializes a new Stack object.
        """
        self.top = None

    def push(self, value):
        """
        Adds a new element to the top of the stack.

        Args:
            value: The value to be added to the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Removes and returns the element from the top of the stack.

        Returns:
            The value of the element removed from the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        """
        Returns the value of the element at the top of the stack without removing it.

        Returns:
            The value of the element at the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.top is None

class Queue:
    def __init__(self):
        """
        Initializes a new Queue object.
        """
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Adds a new element to the rear of the queue.

        Args:
            value: The value to be added to the queue.
        """
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        Returns:
            The value of the element removed from the queue.

        Raises:
            Exception: If the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_value

    def peek(self):
        """
        Returns the value of the element at the front of the queue without removing it.

        Returns:
            The value of the element at the front of the queue.

        Raises:
            Exception: If the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.front is None
