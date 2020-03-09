from node import Node

class Queue: 
    
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        
    def is_empty(self):
        return self.front == self.rear == None
    
    def is_full(self):
        pass

    def size(self):
        return self.length
        
    def enqueue(self, data): #insert
        node = Node(data)
        if self.is_empty():
            self.front = node
        else:
            node.link = self.rear
        self.rear = node
        self.length+=1
        
    def dequeue(self):
        if self.is_empty():
            print('cannot delete from empty queue')
            return -1
        else:
            data = self.front.data
            self.front = self.front.link
            self.length-=1
            return data

    def peek(self):
        return self.front.data

    def display(self):
        pass
        

q = Queue()
q.enqueue(5)
q.enqueue(7)
q.enqueue(8)
print(q.size())
print(q.peek())
print(q.display())
