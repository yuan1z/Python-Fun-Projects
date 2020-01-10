class Stack():
    def __init__(self):
        self.mylist = []
        self.top = None
        self.bottom = None
    def peek(self):
        return self.mylist[-1]
    def push(self,value):
        self.mylist.append(value)
    def pop(self):
        return self.mylist.pop()
    def isEmpty(self):
        x = lambda i : True if len(i)==0 else False
        return x(self.mylist)

if __name__ == "__main__":

    mystack = Stack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)
    print(mystack.isEmpty())
    print(mystack.peek())
    print(mystack.pop())
    print(mystack.peek())
    print(mystack.pop())
    print(mystack.peek())
    print(mystack.pop())
    print(mystack.peek())
    print(mystack.pop())
    #print(mystack.peek())
    print(mystack.isEmpty())
