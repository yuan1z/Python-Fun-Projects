class Node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class BST():
    def __init__(self):
        self.root = None
        self.length = 0
    def insert(self,value,start=None):
        if not start:
            start = self.root
        if self.length == 0:
            self.root = Node(value)
        else:
            if value > start.value:
                if not start.right:
                    start.right = Node(value)
                else:
                    return self.insert(value,start.right)
            else:
                if not start.left:
                    start.left = Node(value)
                else:
                    return self.insert(value,start.left)
        self.length += 1

    def lookup(self,value,start=None):
        if not start:
            start = self.root
        if self.length == 0:
            return False
        if value > start.value and start.right:
            return self.lookup(value,start.right)
        if value < start.value and start.left:
            return self.lookup(value,start.left)
        if value == start.value:
            return start
        return False

    def traverse(self,root):
        if root.left:
            self.traverse(root.left)
        print(root.value)
        if root.right:
            self.traverse(root.right)




if __name__=="__main__":
    tree = BST()
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
