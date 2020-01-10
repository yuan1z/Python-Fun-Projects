class Node():
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.next = None
class linkedlist():
    def __init__(self,node):
        self.head = node
        self.tail = node
        self.length = 1
    def append(self, node):
        self.tail.next = node
        self.tail = node
        self.length+=1
    def prepend(self, node):
        tmp = self.head
        self.head = node
        self.head.next = tmp
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
        else:
            pre,pos = self.lookup(node)
            if pos == self.tail:
                self.tail = pre
                pre.next = None
            else:
                pre.next = pre.next.next
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
            else:
                tmp = pos.next
                pos.next = node
                node.next = tmp
        self.length+=1

    def print_all(self):
        mylist = []
        pos = self.head
        i = 0
        while pos:
            mylist.append((pos.name,pos.value))
            pos = pos.next
        return mylist
    def reverse(self):
        '''
        arr = []
        pos = self.head
        while pos:
            arr.append(pos)
            pos = pos.next
        i = len(arr)-1
        print(i)
        self.head = arr[i]
        self.tail = arr[0]
        while i>=0:
            arr[i].next = arr[i-1]
            i-=1
        self.tail.next = None
        '''
        if not self.head.next:
            return self.head
        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            tmp = second.next
            second.next = first
            first = second
            second = tmp
        self.head.next = None
        self.head = first









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
    mylink.insert(c,a)
    print(mylink.print_all())
    #print(mylink.tail.name)
    #print(mylink.length)
    mylink.reverse()
    print(mylink.print_all())
    print(mylink.tail)