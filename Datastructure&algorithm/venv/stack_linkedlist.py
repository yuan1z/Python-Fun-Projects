class Node():
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.next = None
class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    def peek(self):
        return self.top.name
    def push(self,node):
        if self.length == 0:
            self.top = node
            self.bottom = node
        else:
            tmp = self.top
            self.top = node
            self.top.next = tmp
        self.length+=1
    def pop(self):
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
    mystack = Stack()
    mystack.push(a)
    mystack.push(b)
    mystack.push(c)
    mystack.push(d)
    print(mystack.isEmpty())
    print(mystack.peek())
    print(mystack.pop().name)
    print(mystack.peek())
    print(mystack.pop().name)
    print(mystack.peek())
    print(mystack.pop().name)
    print(mystack.peek())
    print(mystack.pop().name)
    #print(mystack.peek())
    print(mystack.isEmpty())


