class Hash:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx,ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
        if not found:
            self.arr[h].append((key,value))
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for ele in self.arr[h]:
            if ele[0] == key:
                return ele[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,ele in enumerate(self.arr[h]):
            if ele[0] == key:
                del self.arr[h][idx]
                
    
if __name__ == "__main__":
    h = Hash()
    print(h.arr)
    print(h.get_hash('march 6'))
    h['march 6'] = 26
    h['march 9'] = 27
    h['march 17'] = 17
    print(h.arr)
    print(h['march 17'])
    del h['march 6']
    print(h.arr)