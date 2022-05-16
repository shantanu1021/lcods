def isSafe(board, row, col):
    n_rows = len(board)
    n_cols = len(board[0])
    for i in range(n_rows):
        if board[i][col] == 1:
            return False
            
    for j in range(n_cols):
        if board[row][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    # Check lower diagonal on left side
    for i, j in zip(range(row, n_rows, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True

def printSolution(board):
    n_rows = len(board)
    n_cols = len(board[0])
    for i in range(n_rows):
        for j in range(n_cols):
            print (board[i][j], end=" ")
        print()

def solve(board, col):
    n_rows = len(board)
    n_cols = len(board[0])
    for i in range(n_rows):
        if col>=n_cols:
            return True
        if isSafe(board, i, col):
            board[i][col] = 1

            if solve(board, col+1):
                #print(col)
                return True
            
            board[i][col] = 0
    return False

board = []
for i in range(8):
    board.append([])
    for j in range(8):
        board[i].append(0)

if solve(board, 0) == False:
    print("Solution doesnt exist")
else:
    printSolution(board)


# class NQueens_Branch_Bound:
#     def __init__(self,n) -> None:
#         self.n = n
#         self.board = [[0 for i in range(n)] for j in range(n)]
#         # self.slashCode = [[0 for i in range(n)] for j in range(n)]
#         # self.backslashCode = [[0 for i in range(n)] for j in range(n)]
#         self.rowLookUp = [False] * n
#         x = 2 * n - 1
#         self.slashCodeLookup = [False] * x
#         self.backslashCodeLookup = [False] * x

#     def printBoard(self):
#         for i in range(self.n):
#             for j in range(self.n):
#                 if self.board[i][j] == 1:
#                     print("Q",end=" ")
#                 else:
#                     print("-",end=" ")
#             print()
#     def isSafe(self,row,col):
#         if self.slashCodeLookup[row + col] or self.backslashCodeLookup[row - col + self.n - 1] or self.rowLookUp[row]:
#             return False
#         return True
    
#     def recursive(self,col):
#         if col >= self.n:
#             return True
#         for i in range(self.n):
#             if self.isSafe(i,col):
#                 self.board[i][col] = 1
#                 self.rowLookUp[i] = True
#                 self.slashCodeLookup[i + col] = True
#                 self.backslashCodeLookup[i - col + self.n - 1] = True
#                 if self.recursive(col+1):
#                     return True
#                 self.board[i][col] = 0
#                 self.rowLookUp[i] = False
#                 self.slashCodeLookup[i + col] = False
#                 self.backslashCodeLookup[i - col + self.n - 1] = False
#         return False
    
#     def solve(self):
        
#         if self.recursive(0) == False:
#             return False
#         self.printBoard()
#         return True

# solver = NQueens_Branch_Bound(5)
# solver.solve()