# Lab-8: Backtracking: Graph Coloring Problem

def isSafe(graph,n, color):
    '''a function to check if the colored graph is safe or not '''
    for i in range(n): # check for every edge
        for j in range(i + 1, n):
            if (graph[i][j] and color[j] == color[i]):
                return False
    return True
def graphColoring(graph,n, m, i, color):
    '''a function  to solves the graph Coloring problem usingbacktracking.'''
    # if current index reached end
    if i == n:
        if (isSafe(graph,n, color)): # if coloring is safe
            printSolution(color)
            return True
        return False
 
    for j in range(1, m + 1): # Assign each color from 1 to m
        color[i] = j
        if (graphColoring(graph,n, m, i + 1, color)): # Recursive call for the rest vertices.
            return True
        color[i] = 0  # backtracking
    return False
 
def printSolution(color):
    '''A utility function to print solution'''
    print("Solution Exists:" " Following are the assigned colors ")
    for i in range(4):
        print(color[i], end=" ")
 
 
# Driver code
graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
        ]
n = len(graph)
m = 3  # Number of colors
color = [0 for i in range(4)]
 
if (not graphColoring(graph,n, m, 0, color)):
    print("Solution does not exist")