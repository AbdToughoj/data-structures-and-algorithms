from treeIntersection.treeIntersection import Binary_search, tree_intersection

def test_treeIntersection_with_common_values1():
    tree1 = Binary_search()
    tree1.add(5)
    tree1.add(3)
    tree1.add(8)
    tree1.add(2)
    tree1.add(4)

    tree2 = Binary_search()
    tree2.add(3)
    tree2.add(6)
    tree2.add(8)
    tree2.add(2)
    tree2.add(9)

    result = tree_intersection(tree1, tree2)
    assert set(result) == {2, 3, 8}

def test_treeIntersection_with_common_values2():
    tree1 = Binary_search()
    tree1.add(7)
    tree1.add(5)
    tree1.add(10)
    tree1.add(25)
    tree1.add(14)

    tree2 = Binary_search()
    tree2.add(14)
    tree2.add(9)
    tree2.add(10)
    tree2.add(6)
    tree2.add(8)

    result = tree_intersection(tree1, tree2)
    assert set(result) == {10, 14}

def test_tree_intersection_with_no_common_values():

    tree1 = Binary_search()
    tree1.add(5)
    tree1.add(3)
    tree1.add(8)

    tree2 = Binary_search()
    tree2.add(2)
    tree2.add(4)
    tree2.add(9)

    result = tree_intersection(tree1, tree2)
    assert len(result) == 0

