class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        if self.head is None:
            print("The Linked list is empty!")
            return
        
        itr = self.head
        lstr = ""
        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.next 
        print(lstr)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at_beginning(self,data):
        if self.head is None:
            self.head = Node(data,self.head)
            return
        self.head = Node(data,self.head)
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,self.head)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,itr.next)
        
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def insert_at(self,index,data):
        if self.head is None:
            raise Exception("The Linked List is empty!")
        
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index given!")
        
        if index == 0:
            self.head = Node(data,self.head)
            return
            
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data,itr.next)
            itr = itr.next
            count += 1
            
    def remove_at(self,index):
        if self.head is None:
            raise Exception("The Linked List is empty!")
        
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index given!")
        
        if index == 0:
            self.head = self.head.next
            return
            
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            count += 1
            itr = itr.next
            
    def insert_after(self,value,data):
        if self.head is None:
            raise Exception("The Linked list is empty!")
        
        itr = self.head
        while itr:
            if itr.data == value:
                itr.next = Node(data,itr.next) 
                break
            itr = itr.next
            
    def remove_by_value(self,value):
        if self.head is None:
            raise Exception("The Linked list is empty!")
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next
                
if __name__ == "__main__":
    l = LinkedList()
    l.print_list()
    print(l.get_length())
    l.insert_at_beginning(40)
    l.insert_at_beginning(30)
    l.insert_at_beginning(20)
    l.print_list()
    l.insert_at_end(50)
    l.print_list()
    print(l.get_length())
    l.insert_values(['Apple','Orange','Watermelon'])
    l.print_list()
    l.insert_at(0,'Lemon')
    l.insert_at(2,'Grape')
    l.insert_at(5,'Jackfruit')
    l.print_list()
    # l.insert_at(10,'Strawberry')
    l.remove_at(0)
    # l.remove_at(5)
    l.remove_at(2)
    l.print_list()
    l.insert_after('Jackfruit','Strawberry')
    l.insert_after('Grape','Blueberry')
    l.insert_after('Apple','Orange')
    l.print_list()
    l.remove_by_value('Strawberry')
    l.remove_by_value('Apple')
    l.remove_by_value('Watermelon')
    l.print_list()
    