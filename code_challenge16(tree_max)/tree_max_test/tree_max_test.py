from tree_max.tree_max import Tree, Tnode

def test_max_tree():
   tree = Tree()
   tree.root=Tnode(13)
   tree.root.left=Tnode(5)
   tree.root.right=Tnode(8)
   tree.root.left.left=Tnode(18)
   tree.root.left.right=Tnode(16)
   tree.root.right.left=Tnode(0)
   tree.root.right.right=Tnode(7)
   actual=tree.max_tree()
   expected=18
   assert actual==expected


def test_max_tree_empty():
   tree = Tree()
   actual=tree.max_tree()
   expected="No max: the tree is empty"
   assert actual==expected