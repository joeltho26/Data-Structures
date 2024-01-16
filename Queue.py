from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()
        
    def push(self,data):
        self.container.appendleft(data)
    
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
    q = Queue()
    print(q.is_empty())
    q.push(10)
    q.push(20)
    q.push(30)
    q.push(40)
    print(q.is_empty())
    print(q.size())
    print(q.peek())
    q.pop()
    print(q.peek())