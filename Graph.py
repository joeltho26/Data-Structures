class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)
        print(self.graph_dict)
        
    def get_paths(self,start,end,path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths
                
    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]
        
        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path
    
if __name__ == "__main__":
    route = [
        ('Mumbai','Paris'),
        ('Mumbai','Dubai'),
        ('Paris','New York'),
        ('Paris', 'Dubai'),
        ('Dubai','New York'),
        ('New York','Toronto')
    ]
    
    g = Graph(route)
    
    start = "Mumbai"
    end = "New York"
    print(g.get_paths(start,end))
    start_same = "Mumbai"
    end_same = "Mumbai"
    print(g.get_paths(start_same,end_same))
    start_invalid = "Toronto"
    end_invalid = "Mumbai"
    print(g.get_paths(start_invalid,end_invalid))
    
    start_s = "Mumbai"
    end_s = "New York"
    print(g.get_shortest_path(start_s,end_s))
    start_same_s = "Mumbai"
    end_same_s = "Mumbai"
    print(g.get_shortest_path(start_same_s,end_same_s))
    start_invalid_s = "Toronto"
    end_invalid_s = "Mumbai"
    print(g.get_shortest_path(start_invalid_s,end_invalid_s))