class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev = prev
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next 
            count += 1
        return count
    
    def get_last_node(self):
        if self.head is None:
            raise Exception("The Linked list is empty!")
        
        itr = self.head
        while itr.next:
            itr = itr.next 
        return itr
            
    def print_forward(self):
        if self.head is None:
            print("The Linked List is empty!")
            return
            
        itr = self.head
        fstr = "" 
        while itr:
            fstr += str(itr.data) + '-->'
            itr = itr.next
        print(fstr)
    
    def print_backward(self):
        if self.head is None:
            print("The Linked list is empty!")
            return
        
        itr = self.get_last_node()
        bstr = ""
        while itr:
            bstr += '<--' + str(itr.data)
            itr = itr.prev
        print(bstr)
        
    def insert_at_beginning(self,data):
        if self.head is None:
            self.head = Node(None,data,self.head)
            return
        
        node = Node(None,data,self.head)
        self.head.prev = node
        self.head = node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(None,data,self.head)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(itr,data,itr.next)
        itr.next = node
        
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def insert_at(self,index,data):
        if self.head is None:
            raise Exception("The Linked List is empty!")
        
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index given!")
        
        if index == 0:
            node = Node(None,data,self.head)
            self.head.prev = node
            self.head = node
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(itr,data,itr.next)
                if node.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def remove_at(self,index):
        if self.head is None:
            raise Exception("The Linked List is empty!")
        
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index given!")
        
        if index == 0:
            self.head = self.head.next 
            self.head.prev = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                if itr.next.next:
                    itr.next = itr.next.next
                    itr.next.prev = itr
                    break
                itr.next = itr.next.next
            count += 1
            itr = itr.next
    
    def insert_after(self,value,data):
        if self.head is None:
            raise Exception("The Linked List is empty!")
        
        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(itr,data,itr.next)
                if node.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
    
    def remove_by_value(self,value):
        if self.head is None:
            raise Exception("The Linked List is empty!")
        
        if self.head.data == value:
            self.head = self.head.next 
            self.head.prev = None
            return
        
        itr = self.head
        while itr:
            if itr.next.data == value:
                if itr.next.next:
                    itr.next = itr.next.next
                    itr.next.prev = itr
                    break
                itr.next = itr.next.next
            itr = itr.next
    
if __name__ == "__main__":
    l = LinkedList()
    print(l.get_length())
    l.print_forward()
    l.print_backward()
    l.insert_at_beginning(30)
    l.insert_at_beginning(20)
    l.insert_at_beginning(10)
    l.insert_at_end(40)
    l.print_forward()
    l.print_backward()
    l.insert_values(['Apple','Orange','Watermelon'])
    l.print_forward()
    l.print_backward()
    l.insert_at(0,'Lemon')
    l.insert_at(2,'Grape')
    l.print_forward()
    l.insert_at(5,'Jackfruit')
    l.print_forward()
    l.print_backward()
    # l.insert_at(10,'Strawberry')
    l.remove_at(0)
    # l.remove_at(5)
    l.remove_at(2)
    l.print_forward()
    l.print_backward()
    l.insert_after('Jackfruit','Strawberry')
    l.insert_after('Grape','Blueberry')
    l.insert_after('Apple','Orange')
    l.print_forward()
    l.print_backward()
    l.remove_by_value('Strawberry')
    l.remove_by_value('Apple')
    l.remove_by_value('Watermelon')
    l.print_forward()
    l.print_backward()
    
    