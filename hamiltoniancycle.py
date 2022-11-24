# Lab-9: Backtracking: Hamilton Cycle

class Graph:
    def __init__(self,size) -> None:
        self.Nodesize = size 
        self.adjMatrix = [[0]*size for i in range(size)] 
    
    def getGraph(self):
        '''returns the adjacency matrix''' 
        return self.adjMatrix
    
    def add_edge(self,edg):
        '''a method that adds the edges to make a graph'''
        edg = list(edg.split(','))
        edg = [int(i) for i in edg]
        if edg[0] == edg[1] :
            print(f"Same vertex {edg[0]} and {edg[1]}")
        self.adjMatrix[edg[0]][edg[1]] = 1  
        self.adjMatrix[edg[1]][edg[0]] = 1 
 
# main algorithm :
def isSafe(graph, v, path, pos):
    '''a utility function to check if a vertex can be added at index in Hamiltonian Cycle'''
    if graph[path[pos - 1]][v] == 0: 
        return False
    for i in range(pos):
        if path[i] == v:
            return False
    return True
# flag
hasCycle = False

def hamiltonianCycle(graph):
    '''a function to find all hamiltonian cycles in a given graph'''
    global hasCycle
    hasCycle = False # Initially value of flag is false
    path = [] # Store the resultant path
    path.append(0) #initial values are 0
 
    visited = [False]*(len(graph)) # Keeps the track of the visited vertices
    for i in range(len(visited)):
        visited[i] = False
 
    visited[0] = True
    FindHamCycle(graph, 1, path, visited) #a recursive call to find all hamiltonian cycle
    if hasCycle:
        # If no Hamiltonian Cycle is possible for the given graph
        print("No Hamiltonian Cycle possible ")
        return
 
def FindHamCycle(graph, pos, path, visited):
    '''a function to find all the possible hamiltonian cycles'''
    if pos == len(graph):
        if graph[path[-1]][path[0]] != 0: # If there is an edge from the last vertex to the source vertex
            path.append(0)
            for i in range(len(path)-1):
                print(f"{path[i]}",end = " ")
            print("")

            path.pop() # Remove the source vertex added
            hasCycle = True
        return
    for v in range(len(graph)): # Try different vertices as the next vertex
        if isSafe(graph,v, path, pos) and not visited[v]:
            path.append(v)
            visited[v] = True
            FindHamCycle(graph, pos + 1, path, visited) # recursive call
            visited[v] = False  # backtrack Remove current vertex from path and process other vertices
            path.pop()

# driver code                 
g = Graph(6)
g.add_edge('0,2')                                           
g.add_edge('0,1')                                           
g.add_edge('0,5')                                           
g.add_edge('1,2')                                           
g.add_edge('1,5')                                           
g.add_edge('1,4')                                           
g.add_edge('2,3')                                           
g.add_edge('3,4')                                           
g.add_edge('4,5')                                           

hamiltonianCycle(g.getGraph())
