# BST (array)

class BST:
    
    MAX = 15
    
    def __init__(self):
        self.tree = [-1 for i in range(self.MAX)]
        
    def insert(self, data):
        curr = 0
        
        while curr < self.MAX:
            if self.tree[curr] == -1:
                self.tree[curr] = data
                break
                
            elif data < self.tree[curr]:
                curr = curr * 2 + 1
                
            else:
                curr = curr * 2 + 2
                
    def search(self, target):
        curr = 0
        found = False
        
        while curr < self.MAX and not found:
            if self.tree[curr] == target:
                print("Found!")
                found = True
                
            elif target < self.tree[curr]:
                curr = curr * 2 + 1
                
            else:
                curr = curr * 2 + 2
                
        if not found:
            print("Not found!")
                
                
    def minimum(self):
        curr = 0
        
        while curr*2+1 < self.MAX and self.tree[curr*2+1] != -1:
            curr = curr * 2 + 1
            
        print(self.tree[curr])
        
    def maximum(self):
        curr = 0
        
        while curr*2+2 < self.MAX and self.tree[curr*2+2] != -1:
            curr = curr * 2 + 2
            
        print(self.tree[curr])
        
    def inorder(self, curr=0):
        if curr*2+1 < self.MAX and self.tree[curr*2+1] != -1:
            self.inorder(curr*2+1)
        print(self.tree[curr], end=' ')
        if curr*2+2 < self.MAX and self.tree[curr*2+2] != -1:
            self.inorder(curr*2+2)
            
    def preorder(self, curr=0):
        print(self.tree[curr], end=' ')
        if curr*2+1 < self.MAX and self.tree[curr*2+1] != -1:
            self.preorder(curr*2+1)
        if curr*2+2 < self.MAX and self.tree[curr*2+2] != -1:
            self.preorder(curr*2+2)
            
    def postorder(self, curr=0):
        if curr*2+1 < self.MAX and self.tree[curr*2+1] != -1:
            self.postorder(curr*2+1)
        if curr*2+2 < self.MAX and self.tree[curr*2+2] != -1:
            self.postorder(curr*2+2)
        print(self.tree[curr], end=' ')
            
    def reverse(self, curr=0):
        if curr*2+2 < self.MAX and self.tree[curr*2+2] != -1:
            self.reverse(curr*2+2)
        print(self.tree[curr], end=' ')
        if curr*2+1 < self.MAX and self.tree[curr*2+1] != -1:
            self.reverse(curr*2+1)
            
            
            
# main
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(80)
bst.insert(10)
bst.insert(40)
bst.insert(70)
bst.insert(90)
bst.inorder()
print()
bst.preorder()
print()
bst.postorder()
print()
bst.reverse()
print()
bst.search(80)
bst.search(100)
bst.minimum()
bst.maximum()
