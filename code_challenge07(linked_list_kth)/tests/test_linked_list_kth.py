from linked_list_kth.linked_list_kth import LinkedList
def test_kthFromEnd_greater_than_length():
    ll = LinkedList()
    ll.append(1)
    ll.append(4)
    ll.append(8)
    ll.append(2)

    actual = ll.kthFromEnd(5)
    expected = "Exception"

    assert actual == expected

def test_kthFromEnd_same_k_and_length():
    ll = LinkedList()
    ll.append(1)
    ll.append(4)
    ll.append(8)
    ll.append(2)

    actual = ll.kthFromEnd(4)
    expected = "Exception"

    assert actual == expected

def test_kthFromEnd_negative_k():
    ll = LinkedList()
    ll.append(1)
    ll.append(4)
    ll.append(8)
    ll.append(2)

    actual = ll.kthFromEnd(-2)
    expected = "Exception"

    assert actual == expected

def test_kthFromEnd_size_one():
    ll = LinkedList()
    ll.append(5)

    actual = ll.kthFromEnd(0)
    expected = 5

    assert actual == expected

def test_kthFromEnd_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(4)
    ll.append(8)
    ll.append(2)

    actual = ll.kthFromEnd(2)
    expected = 4

    assert actual == expected


