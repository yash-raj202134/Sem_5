# Lab 5 :
# Design a "Graph" class that represent a Graph 
# where edges are represented as 
# {Node1: (Node2, Weight1), Node2: (Node3, Weight2)}

class Graph:
    def __init__(self,no_of_nodes) -> None:
        self.No_of_node = no_of_nodes
        
        self.adjList={node :set() for node in range(self.No_of_node)}
    
    def add_edge(self,node1,node2,weight=1):
        self.adjList[node2].add((node1,weight))
        
    
    def printGr(self):
        for item in self.adjList.keys():
            print("node" ,item , ": ",self.adjList[item])



g = Graph(4)

g.add_edge(0, 0, 25)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 1)
g.add_edge(1, 4, 15)
g.add_edge(4, 2, 7)
g.add_edge(4, 3, 11)
