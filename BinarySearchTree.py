class TreeNode:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)
        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)
    
    def inorder_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.inorder_traversal()
            
        elements.append(self.data)
        
        if self.right:
            elements += self.right.inorder_traversal()
            
        return elements
    
    def preorder_traversal(self):
        elements = []
        
        elements.append(self.data)
        
        if self.left:
            elements += self.left.inorder_traversal()
        
        if self.right:
            elements += self.right.inorder_traversal()
            
        return elements
    
    def postorder_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.inorder_traversal()
        
        if self.right:
            elements += self.right.inorder_traversal()
            
        elements.append(self.data)
            
        return elements
    
    def search(self,data):
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        elif data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False
    
    def delete(self,data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.right is None and self.left is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        
        return self
                
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    
    def calculate_sum(self):
        left = 0
        right = 0
        if self.left:
            left += self.left.calculate_sum()
        
        if self.right:
            right += self.right.calculate_sum()
            
        return left + self.data + right
    
def build_tree(elements):
    root = TreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
    
if __name__ == '__main__':
    numbers = [15,12,7,14,27,20,23,88 ]
    print(build_tree(numbers).inorder_traversal())
    print(build_tree(numbers).preorder_traversal())
    print(build_tree(numbers).postorder_traversal())
    print(build_tree(numbers).search(24))
    print(build_tree(numbers).search(23))
    print(build_tree(numbers).find_max())
    print(build_tree(numbers).find_min())
    print(build_tree(numbers).calculate_sum())
    tree = build_tree(numbers).delete(27)
    print(tree.inorder_traversal())