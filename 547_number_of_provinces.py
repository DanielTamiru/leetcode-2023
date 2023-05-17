from typing import List

### Recursive DFS ### 

class Solution1:
    visited: set

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        
        self.visited = set()
        for city, neighbours in enumerate(isConnected):
            if city not in self.visited: 
                self.DFS(city, isConnected)
                count += 1
        
        return count

    def DFS(self, city, graph):
        self.visited.add(city)
        
        for neighbour, exists in enumerate(graph[city]):
            if exists and neighbour not in self.visited:
                self.DFS(neighbour, graph)
                

### Iterative DFS ### 

class Solution2:
    visited: set

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        
        self.visited = set()

        for city, neighbours in enumerate(isConnected):
            if city not in self.visited: 
                self.DFS(city, isConnected)
                count += 1
        
        return count


    def DFS(self, city, graph):
        to_visit = [city]

        while to_visit:
            city = to_visit.pop()
            self.visited.add(city)
            
            for neighbour, exists in enumerate(graph[city]):
                if exists and neighbour not in self.visited:
                    to_visit.append(neighbour)


### Iterative BFS ### 

from queue import Queue

class Solution3:
    visited: set

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        
        self.visited = set()

        for city, neighbours in enumerate(isConnected):
            if city not in self.visited: 
                self.BFS(city, isConnected)
                count += 1
        
        return count


    def BFS(self, city, graph):
        to_visit = Queue()
        to_visit.put(city)

        while not to_visit.empty():
            city = to_visit.get()
            self.visited.add(city)
            
            for neighbour, exists in enumerate(graph[city]):
                if exists and neighbour not in self.visited:
                    to_visit.put(neighbour)
