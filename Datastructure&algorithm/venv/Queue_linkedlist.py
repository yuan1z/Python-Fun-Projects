class Node():
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.next = None
class Queue():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    def peek(self):
        return self.top.name
    def enqueue(self,node):
        if self.length == 0:
            self.top = node
            self.bottom = node
        else:
            self.bottom.next = node
            self.bottom = node
        self.length+=1
    def dequeue(self):
        self.length-=1
        if self.top == self.bottom:
            tmp = self.top
            self.bottom = None
            self.top = None
        else:
            tmp = self.top
            self.top = self.top.next
        return tmp
    def isEmpty(self):
        if not self.top and not self.bottom:
            return True
        else:
            return False

if __name__ == "__main__":
    a = Node('a',1)
    b = Node('b',2)
    c = Node('c',3)
    d = Node('d',4)
    mystack = Queue()
    mystack.enqueue(a)
    mystack.enqueue(b)
    mystack.enqueue(c)
    mystack.enqueue(d)
    print(mystack.isEmpty())
    print(mystack.peek())
    print(mystack.dequeue().name)
    print(mystack.peek())
    print(mystack.dequeue().name)
    print(mystack.peek())
    print(mystack.dequeue().name)
    print(mystack.peek())
    print(mystack.dequeue().name)
    #print(mystack.peek())
    print(mystack.isEmpty())


