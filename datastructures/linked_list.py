from node import Node
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def add(self, value):
        temp = Node(value)
        temp.set_link(self.head)
        self.head = temp

    def size(self):
        curr = self.head
        count = 0
        while curr != None:
            count+=1
            curr = curr.get_link() #curr = curr.link
        return count

    def search(self, target):
        curr = self.head
        found=False
        count=0
        while curr != None and not found:
            count+=1
            if curr.get_data() == target: #curr.data == target
                found=True
            else:
                curr = curr.get_link() # curr = curr.link
        return found, count

    def display(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.get_link()

        
if __name__=="__main__":
    LL1 = LinkedList()
    LL1.add(34)
    LL1.add(5)
    LL1.add(99)
    print(LL1.search(99))
    print(LL1.search(12))
