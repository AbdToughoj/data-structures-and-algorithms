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

def kthFromEnd(self, k):
    if not self.head or k < 0:
        return "Exception"

    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next

    if k >= count:
        return "Exception"

    current = self.head
    for _ in range(count - k - 1):
        current = current.next

    return current.value