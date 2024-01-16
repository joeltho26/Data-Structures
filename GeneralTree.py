class TreeNode:
    def __init__(self, data=None):
        self.data = data 
        self.children = [] 
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        itr = self.parent
        while itr:
            itr = itr.parent
            level += 1
        return level 
        
    def print_tree(self):
        spaces = " " * self.get_level() * 2
        prefix = spaces + '|--' if self.parent else ""
        print(prefix + str(self.data))
        if self.children:
            for child in self.children:
                child.print_tree()
    
def build_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Apple"))
    laptop.add_child(TreeNode("Samsung"))
    laptop.add_child(TreeNode("Acer"))
    
    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("Apple"))
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("Pixel"))
    
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Micromax"))
    tv.add_child(TreeNode("LG"))
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    return root

if __name__ == "__main__":
    build_tree().print_tree()