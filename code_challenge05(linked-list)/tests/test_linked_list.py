from linked_list.linked_list import LinkedList

def test_instantiate_empty_linked_list():
    linked_list = LinkedList()
    expected = ' -> NONE'  
    assert linked_list.to_string() == expected

def test_insert_into_linked_list():
    linked_list = LinkedList()
    linked_list.insert('1')
    linked_list.insert('2')
    linked_list.insert('3')
    expected = '3 -> 2 -> 1 -> NONE'  
    assert linked_list.to_string() == expected

def test_head_property():
    linked_list = LinkedList()
    linked_list.insert('1')
    linked_list.insert('2')
    linked_list.insert('3')
    expected = '3'  
    assert linked_list.head.value == expected

def test_insert_multiple_nodes():
    linked_list = LinkedList()
    linked_list.insert('3')
    linked_list.insert('2')
    linked_list.insert('1')
    expected = '1 -> 2 -> 3 -> NONE'  
    assert linked_list.to_string() == expected

def test_includes_existing_value():
    linked_list = LinkedList()
    linked_list.insert('4')
    linked_list.insert('5')
    linked_list.insert('6')
    value = '5'  
    expected = True
    assert linked_list.includes(value) == expected

def test_includes_nonexistent_value():
    linked_list = LinkedList()
    linked_list.insert('2')
    linked_list.insert('4')
    linked_list.insert('8')
    value = '5' 
    expected = False
    assert linked_list.includes(value) == expected

def test_return_all_values():
    linked_list = LinkedList()
    linked_list.insert('c')
    linked_list.insert('b')
    linked_list.insert('a')
    expected = 'a -> b -> c -> NONE'  
    assert linked_list.to_string() == expected


