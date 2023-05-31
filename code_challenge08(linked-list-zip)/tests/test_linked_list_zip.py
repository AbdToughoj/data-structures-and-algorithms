from linked_list_zip.linked_list_zip import LinkedList,zipLists
def test_zipLists_equal_lengths():
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)

    list2 = LinkedList()
    list2.append('A')
    list2.append('B')
    list2.append('C')

    result = zipLists(list1, list2)

    expected = "1 -> A -> 2 -> B -> 3 -> C -> NONE"
    actual = result.to_string()
    assert actual == expected


def test_zipLists_list1_longer():
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)

    list2 = LinkedList()
    list2.append('A')
    list2.append('B')

    result = zipLists(list1, list2)

    expected = "1 -> A -> 2 -> B -> 3 -> 4 -> NONE"
    actual = result.to_string()
    assert actual == expected


def test_zipLists_list1_shorter():
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)

    list2 = LinkedList()
    list2.append('A')
    list2.append('B')
    list2.append('C')
    list2.append('D')

    result = zipLists(list1, list2)

    expected = "1 -> A -> 2 -> B -> C -> D -> NONE"
    actual = result.to_string()
    assert actual == expected
