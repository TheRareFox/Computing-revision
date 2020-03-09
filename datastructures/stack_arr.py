# array version using pre-initialized values of 0
class Stack1:
    
    MAX = 10
    
    def __init__(self):
        self.data = [0 for i in range(self.MAX)] 
        self.top = -1
        
    def is_empty(self):
        return self.top == -1
        
    def is_full(self):
        return self.top == (self.MAX - 1)
    
    def push(self, data):
        if self.is_full():
            print("Cannot insert to full stack")
            return -1
        else: #can insert
            self.top+=1
            self.data[self.top] = data
            
    def pop(self): #delete
        if self.is_empty():
            print('Cannot delete from empty stack')
            return -1
        else:
            data = self.data[self.top]
            self.top -= 1
            return data

    def peek(self):
        if not self.is_empty():
            return self.data[self.top]
        return None
        
    def display(self):
        i = self.top
        while i >= 0:
            print(self.data[i], end = ' ')
            i-=1
        print()

# alternative array version dynamic sizing of array

class Stack2:
    
    MAX = 10
    
    def __init__(self):
        self.data = []

    def is_full(self):
        return len(self.data) == self.MAX
    
    def is_empty(self):
        return len(self.data) == 0
        
    def push(self, data):
        if len(self.data) == self.MAX:
            print('Cannot push to full stack')
        else:
            self.data.append(data)
            
    def pop(self):
        if len(self.data) == 0:
            print('Cannot delete from empty stack')
        else:
            del self.data[-1]

    def peek(self):
        if not self.is_empty:
            return self.data[-1]
        return None
    
    def display(self):
        print(self.data)

if __name__=="__main__":
    print("Stack1:")
    s = Stack1()
    print(s.peek())
    s.push(6)
    s.push(5)
    s.push(8)
    s.display()
    print(s.peek())
    s.pop()
    s.display()
    print("\nStack2:")

    s = Stack2()
    print(s.peek())
    s.push(6)
    s.push(5)
    s.push(8)
    s.display()
    print(s.peek())
    s.pop()
    s.display()
    
