class Node():
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.next = None
        self.parent = None
class linkedlist():
    def __init__(self,node):
        self.head = node
        self.tail = node
        self.length = 1
    def append(self, node):
        self.tail.next = node
        node.parent = self.tail
        self.tail = node
        node.next = None
        self.length+=1
    def prepend(self, node):
        tmp = self.head
        self.head = node
        self.head.next = tmp
        tmp.parent = self.head
        self.head.parent = None
        self.length+=1
    def lookup(self,node):
        position = self.head
        pre = None
        while position != node:
            if position == self.tail:
                return None
            else:
                pre = position
                position = position.next
        return (pre,position)
    def delete(self,node):
        if node == self.head:
            self.head = node.next
            self.head.parent = None
        else:
            pre,pos = self.lookup(node)
            if pos == self.tail:
                self.tail = pre
                pre.next = None
            else:
                pre.next = pre.next.next
                pre.next.parent = pre
        self.length-=1

    def insert(self,position,node):
        if self.lookup(node)!=None:
            raise ValueError('linkedin list is circled')
        else:
            pre,pos = self.lookup(position)
            if pos == self.tail:
                pos.next = node
                node.next = None
                self.tail = node
                self.tail.parent = pos
            else:
                tmp = pos.next
                pos.next = node
                node.next = tmp
                node.next.parent = node
                node.parent = pos
        self.length+=1

    def print_all(self):
        mylist = []
        pos = self.head
        while pos:
            print(pos.value)
            mylist.append((pos.name,pos.value))
            pos = pos.next
        return mylist





if __name__ == "__main__":
    a = Node('a',1)
    b = Node('b',2)
    c = Node('c',3)
    d = Node('d',4)
    mylink = linkedlist(a)
    mylink.append(b)
    mylink.append(c)
    mylink.prepend(d)

    print(mylink.print_all())
    mylink.delete(a)
    print(mylink.print_all())
    mylink.insert(d,a)
    print(mylink.print_all())
    #print(mylink.tail.name)
    #print(mylink.length)
    print(a.parent.name)