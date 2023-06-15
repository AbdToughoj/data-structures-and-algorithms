from Trees.Trees import Tree, Tnode,Binary_search

def test_pre_order():
   trees = Tree()
   trees.root=Tnode(5)
   trees.root.left=Tnode(10)
   trees.root.right=Tnode(4)
   trees.root.left.left=Tnode(6)
   trees.root.left.right=Tnode(8)
   trees.root.right.left=Tnode(7)
   trees.root.right.right=Tnode(18)
   actual=trees.pre_order()
   expected=[5, 10, 6, 8, 4, 7, 18]
   assert actual==expected

def test_in_order():
   trees = Tree()
   trees.root=Tnode(5)
   trees.root.left=Tnode(10)
   trees.root.right=Tnode(4)
   trees.root.left.left=Tnode(6)
   trees.root.left.right=Tnode(8)
   trees.root.right.left=Tnode(7)
   trees.root.right.right=Tnode(18)
   actual=trees.in_order()
   expected=[6, 10, 8, 5, 7, 4, 18]
   assert actual==expected
   
def test_post_order():
   trees = Tree()
   trees.root=Tnode(5)
   trees.root.left=Tnode(10)
   trees.root.right=Tnode(4)
   trees.root.left.left=Tnode(6)
   trees.root.left.right=Tnode(8)
   trees.root.right.left=Tnode(7)
   trees.root.right.right=Tnode(18)
   actual=trees.post_order()
   expected=[6, 8, 10, 7, 18, 4, 5]
   assert actual==expected

def test_empty_tree():
   trees = Tree()
   actual=trees.pre_order()
   expected=None
   assert actual==expected

def test_one_tnode_tree():
      trees = Tree()
      trees.root=Tnode('root')
      actual=trees.pre_order()
      expected=['root']
      assert actual==expected

def test_binary_tree():
   binary=Binary_search()
   binary.add(6)
   binary.add(5)
   binary.add(9)
   binary.add(7)
   binary.add(10)
   binary.add(12)
   binary.add(15)
   actual=binary.in_order()
   expected=[5, 6, 7, 9, 10, 12, 15]
   assert actual==expected

def test_contain_true():
   binary=Binary_search()
   binary.add(6)
   binary.add(5)
   binary.add(9)
   binary.add(7)
   binary.add(10)
   binary.add(12)
   binary.add(15)
   actual=binary.contains(7)
   expected=True
   assert actual==expected

def test_contain_false():
   binary=Binary_search()
   binary.add(6)
   binary.add(5)
   binary.add(9)
   binary.add(7)
   binary.add(10)
   binary.add(12)
   binary.add(15)
   actual=binary.contains(30)
   expected=False
   assert actual==expected