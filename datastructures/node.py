class Node:
    def __init__(self, data=0):
        self.data = data
        self.link = None
    
    def get_data(self):
        return(self.data)
    
    def set_data(self, new_data):
        self.data = new_data
        
    def get_link(self):
        return self.link
    
    def set_link(self, new_link):
        self.link = new_link

if __name__=="__main__":
    n = Node(5)
    print(n.get_data())
