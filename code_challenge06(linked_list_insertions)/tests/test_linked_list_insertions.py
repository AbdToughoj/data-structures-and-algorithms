from linked_list_insertions.linked_list_insertions import LinkedList

def test_append():
    linked_list = LinkedList()

    linked_list.append(1)

    actual = linked_list.to_string()
    expected = "1 -> NONE"

    assert actual == expected

def test_append_multiple_nodes():
    linked_list = LinkedList()

    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    actual = linked_list.to_string()
    expected = "1 -> 2 -> 3 -> 4 -> 5 -> NONE"

    assert actual == expected

def test_insert_before_middle_node():
    linked_list = LinkedList()

    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)

    linked_list.insert_before(3, 5)

    actual = linked_list.to_string()
    expected = "4 -> 5 -> 3 -> 2 -> 1 -> NONE"

    assert actual == expected


def test_insert_before_first_node():
    linked_list = LinkedList()

    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    linked_list.insert_before(3, 4)

    actual = linked_list.to_string()
    expected = "4 -> 3 -> 2 -> 1 -> NONE"

    assert actual == expected

def test_insert_after_middle_node():
    linked_list = LinkedList()

    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    linked_list.insert_after(2, 4)

    actual = linked_list.to_string()
    expected = "3 -> 2 -> 4 -> 1 -> NONE"

    assert actual == expected

def test_insert_after_last_node():
    linked_list = LinkedList()

    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    linked_list.insert_after(1, 4)

    actual = linked_list.to_string()
    expected = "3 -> 2 -> 1 -> 4 -> NONE"

    assert actual == expected





