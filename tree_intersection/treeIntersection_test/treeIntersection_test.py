from treeIntersection.treeIntersection import Binary_search
# import tree_intersection.tree_intersection.Binary_search

def test_treeIntersection_with_common_values():
    # Test when both trees have common values
    # Arrange
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

    # # Act
    # result = treeIntersection(tree1, tree2)

    # # Assert
    # assert set(result) == {2, 3, 8}