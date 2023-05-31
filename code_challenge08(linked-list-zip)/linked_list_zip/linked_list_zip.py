class Node:
    def __init__(self, value):
        """
        Initializes a new instance of the Node class.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Initializes a new instance of the LinkedList class.
        """
        self.head = None

    def append(self, value):
        """
        Appends a new node with the given value to the linked list.

        Args:
            value: The value to be appended to the linked list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

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


def zipLists(list1, list2):
    """
    Zips two linked lists together into one, alternating nodes between the two lists.

    Args:
        list1: The first linked list.
        list2: The second linked list.

    Returns:
        A new linked list that contains nodes from list1 and list2 alternately.
    """
    if not list1.head:
        return list2
    if not list2.head:
        return list1

    starting_head = Node(None)
    current = starting_head

    while list1.head and list2.head:
        current.next = list1.head
        list1.head = list1.head.next
        current = current.next

        current.next = list2.head
        list2.head = list2.head.next
        current = current.next

    if list1.head:
        current.next = list1.head

    if list2.head:
        current.next = list2.head

    result = LinkedList()
    result.head = starting_head.next

    return result
