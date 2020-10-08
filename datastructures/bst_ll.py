# BST (linked list)

class BST:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = BST(data)
            else:
                self.left.insert(data)
                
        else:
            if self.right == None:
                self.right = BST(data)
            else:
                self.right.insert(data)
                
    def search(self, target):
        if self.data == target:
            print("Found!")
            
        elif target < self.data:
            if self.left == None:
                print("Not found!")
            else:
                self.left.search(target)
                
        else:
            if self.right == None:
                print("Not found!")
            else:
                self.right.search(target)
                
    def lookup(self, target, parent=None):
        if self.data == target:
            return self, parent
        
        elif target < self.data:
            if self.left == None:
                return None, None
            else:
                return self.left.lookup(target, self)
            
        else:
            if self.right == None:
                return None, None
            else:
                return self.right.lookup(target, self)
            
    def delete(self, target):
        child, parent = self.lookup(target)
        
        if child == None:
            print("Not found!")
            
        else:
            if child.left == child.right == None: # 0 child
                if parent == None:
                    child = None
                    
                else:
                    if parent.left == child:
                        parent.left = None
                    else:
                        parent.right = None
                        
            elif (child.left == None) != (child.right == None): # 1 child
                if child.left:
                    node = child.left
                else:
                    node = child.right
                    
                if parent == None:
                    child = node
                
                else:
                    if parent.left == child:
                        parent.left = node
                    else:
                        parent.right = node
                        
            else: # 2 children
                node = None
                successor = child.left
                while successor.right:
                    node = successor
                    successor = successor.right
                    
                child.data = successor.data
                
                if node:
                    node.right = successor.left
                else:
                    child.left = successor.left
                    
    def minimum(self):
        if self.left == None:
            print(f"Minimum: {self.data}")
        else:
            self.left.minimum()
            
    def maximum(self):
        if self.right == None:
            print(f"Maximum: {self.data}")
        else:
            self.right.maximum()
            
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder()
            
    def preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
            
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=' ')
        
    def reverse(self):
        if self.right:
            self.right.reverse()
        print(self.data, end=' ')
        if self.left:
            self.left.reverse()
            
            
            
# main
bst = BST(50)
bst.insert(30)
bst.insert(80)
bst.insert(10)
bst.insert(40)
bst.insert(70)
bst.insert(90)
bst.insert(60)
bst.insert(75)
bst.insert(73)
bst.inorder()
print()
bst.preorder()
print()
bst.postorder()
print()
bst.reverse()
print()
bst.delete(90) # 0 child
bst.delete(70) # 1 child
bst.delete(50) # 2 children
bst.delete(80) # 2 children
print("after")
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
