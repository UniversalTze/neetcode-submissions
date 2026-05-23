class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # space = o (n^2) 
        # time = o (n^2)
        # n represents the number of rows in square grid

        # using set to check for duplicates. 
        # column wise is also the same
        # row check -> simple iterate through a row with a set. 
        
        # Formula: 
        # board[i][j] will be indexes. 
        # (0,0), (0,1), (0,2), (1,0), (1,1), (1,2)...
        # (0,3), (0,4), (0,5),(1,5)
        # board[i][j] = row
        # boord[j][i] = column
        for i in range(len(board)): 
            # reset for each row and column
            seenRow = set() 
            seenColumn = set()
            for j in range(len(board[i])):
                if board[i][j] != ".": 
                    if board[i][j] in seenRow: 
                        return False
                    seenRow.add(board[i][j]) # for row set
                
                if board[j][i] != ".": 
                    if board[j][i] in seenColumn: 
                        return False
                    seenColumn.add(board[j][i]) # for column set
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

                
        return True
        