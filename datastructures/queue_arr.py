# queue class
# array version

class Queue:
    
    MAX = 5 # queue can only store MAX-1
    
    def __init__(self):
        self.queue = []
        for i in range(self.MAX):
            self.queue.append(0)
        self.front = 0 # location to delete
        self.rear = 0 # location to insert
        
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return self.size() == self.MAX - 1
    
    def size(self):
        if self.is_empty():
            return 0
        elif self.front < self.rear:
            return self.rear - self.front
        else: # rear is in front ie wraparound
            return self.rear + self.MAX - self.front
        
    def enqueue(self, data): # insert
        if self.is_full():
            print("Cannot insert to full queue")
            return -1
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % self.MAX
        
    def dequeue(self): # delete
        if self.is_empty():
            print("Cannot delete from empty queue")
            return -1
        else:
            data = self.queue[self.front]
            self.front = (self.front + 1) % self.MAX
            return data
        
    def peek(self):
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Empty queue")
        else:
            if self.front < self.rear:
                for i in range(self.front, self.rear):
                    print(self.queue[i], end=' ')
            else: # wraparound
                for j in range(self.front, self.MAX):
                    print(self.queue[j], end=' ')
                for k in range(0, self.rear):
                    print(self.queue[k], end=' ')
        print()

        
        
# main
q = Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(99)
q.enqueue(77)
q.enqueue(88)
q.display()
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(55)
q.display()
#print(q.dequeue())
#print(q.dequeue())
