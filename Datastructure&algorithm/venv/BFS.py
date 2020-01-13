import BST

if __name__=="__main__":
    tree = BST.BST()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    print(tree.root.right.right.value)
    print(tree.lookup(170))
    tree.traverse(tree.root)
    print(tree.BFS())
    print(tree.BFSR([tree.root],[]))
    print(tree.DFSInorder(tree.root,[]))
    print(tree.DFSPreorder(tree.root, []))
    print(tree.DFSPostorder(tree.root, []))