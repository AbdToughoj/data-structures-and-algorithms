from linked_list_zip.linked_list_zip import LinkedList,zipLists
def test_zipLists():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2 = LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    result = zipLists(list1, list2)

    assert result.head.value == 1
    assert result.head.next.value == 5
    assert result.head.next.next.value == 3
    assert result.head.next.next.next.value == 9
    assert result.head.next.next.next.next.value == 2
    assert result.head.next.next.next.next.next.value == 4
    assert result.head.next.next.next.next.next.next is None

def test_zipLists_emptyList():
    list1 = LinkedList()

    list2 = LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    result = zipLists(list1, list2)

    assert result.head.value == 5
    assert result.head.next.value == 9
    assert result.head.next.next.value == 4
    assert result.head.next.next.next is None