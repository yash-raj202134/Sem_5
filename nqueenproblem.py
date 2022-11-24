# Lab-7: Backtracking: N-Queens

def board(n: int) -> list:
    '''a function to create a board '''
    b = [[0 for i in range(n)]for j in range(n)]
    return b

def isSafe(board, row, col, n) -> bool:
    '''a utility function to check whether a queen can be placed 
       at a particular position or not'''
    i = j = 0
    # check left side of row.
    for i in range(0, col):
        if board[row][i] == 1:
            return False
    # Now check upper diagonal on left.
    i, j = row, col
    while(i >= 0 and j >= 0):
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # check lower diagonal on left
    i, j = row, col
    while(j >= 0 and i < n):
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def solveNqueen(board, col, n):
    '''a function to solve n queen problem.'''
    # Base condition
    if col >= n:  # if all queens are placed.
        return True
    # Try placing queen in all rows one by one , fixing 1 column.
    for i in range(0, n):
        if isSafe(board, i, col, n):  # constrain.
            board[i][col] = 1  # place the queen on board.
            # next, recursive call to place other queen(s)
            next = solveNqueen(board, col+1, n)
            if next:
                return True
            # Backtracking or removing the queen
            board[i][col] = 0

    return False  # if queen is not placed

def printboard(board):
    '''a utility function to print the solution of n-queen or board'''
    for item in board:
        print(item, end='\n')
    print("\t")
    # Calculate another position of queens by taking transpose of the previous solution
    tp = [[board[j][i] for j in range(len(board))]
          for i in range(len(board[0]))]
    for item in tp:
        print(item, end='\n')
    return

# Driver code
board = board(4)  # creates a board of nxn
result = solveNqueen(board, 0, 4)
if result == True:
    printboard(board)
