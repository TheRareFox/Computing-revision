from node import Node

class Stack:
    
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top == None
        
    def is_full(self):
        pass # impossible
    
    def push(self, data):
        if self.is_full():
            print("Yo you have reached the impossible")
            return -1
        else:
            node = Node(data)
            node.link = self.top
            self.top = node
        
    def pop(self):
        if self.is_empty():
            print("Cannot delete from empty stack")
            return -1
        else:
            data = self.top.data
            self.top = self.top.link
            return data
        
    def peek(self):
        if not self.is_empty():
            return self.top.data
        
    def display(self):
        curr = self.top
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.link
        print()

if __name__=="__main__":
    print("Stack:")
    s = Stack()
    print(s.peek())
    s.push(6)
    s.push(5)
    s.push(8)
    s.display()
    print(s.peek())
    s.pop()
    s.display()
