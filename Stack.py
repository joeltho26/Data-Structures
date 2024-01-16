from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self,data):
        self.container.append(data)
    
    def pop(self):
        self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)
    
    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            return False
    
if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.is_empty())
    print(s.size())
    print(s.peek())
    s.pop()
    print(s.peek())