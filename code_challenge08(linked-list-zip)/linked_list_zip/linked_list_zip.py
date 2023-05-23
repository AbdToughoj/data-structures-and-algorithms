class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def zipLists(list1, list2):
    # Edge cases: if either list is empty, return the other list
    if not list1.head:
        return list2
    if not list2.head:
        return list1

    # Create a dummy head node for the new linked list
    dummy_head = Node(None)
    current = dummy_head

    while list1.head and list2.head:
        # Take a node from list1 and append it to the new list
        current.next = list1.head
        list1.head = list1.head.next
        current = current.next

        # Take a node from list2 and append it to the new list
        current.next = list2.head
        list2.head = list2.head.next
        current = current.next

    # If list1 still has remaining nodes, append them to the new list
    if list1.head:
        current.next = list1.head

    # If list2 still has remaining nodes, append them to the new list
    if list2.head:
        current.next = list2.head

    # Create a new linked list instance and set its head
    result = LinkedList()
    result.head = dummy_head.next

    return result