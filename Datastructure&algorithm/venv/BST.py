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
    def BFS(self):
        currentNode = self.root
        mylist = []
        queue = []
        mylist.append(currentNode.value)
        queue.append(currentNode)
        while len(queue)!=0:
            currentNode = queue.pop(0)
            if currentNode.left:
                queue.append(currentNode.left)
                mylist.append(currentNode.left.value)
            if currentNode.right:
                queue.append(currentNode.right)
                mylist.append(currentNode.right.value)
        return mylist

    def BFSR(self,queue,mylist):
        if len(queue)==0:
            return mylist
        else:
            currentNode = queue.pop(0)
            mylist.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            return self.BFSR(queue,mylist)
    def DFSInorder(self,root,mylist):
        if root.left:
            self.DFSInorder(root.left,mylist)
        mylist.append(root.value)
        if root.right:
            self.DFSInorder(root.right,mylist)
        return mylist
    def DFSPreorder(self,root,mylist):
        mylist.append(root.value)
        if root.left:
            self.DFSPreorder(root.left,mylist)
        if root.right:
            self.DFSPreorder(root.right,mylist)
        return mylist
    def DFSPostorder(self,root,mylist):
        if root.left:
            self.DFSPostorder(root.left, mylist)
        if root.right:
            self.DFSPostorder(root.right, mylist)
        mylist.append(root.value)
        return mylist




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
