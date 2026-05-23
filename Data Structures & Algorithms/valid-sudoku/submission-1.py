class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # space = o (n^2) 
        # time = o (n^2)
        # n represents the number of rows in square grid

        # using set to check for duplicates. 
        # column wise is also the same
        # row check -> simple iterate through a row with a set. 
        
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
        
        # calculate equation for seenSquare again (for understanding)
        for num in range(9): 
            # theres is 9 (3 * 3) squares on a 9 * 9 Sudoku Board
            # 0th Square -> (0,0), (0,1), (0,2), (1,0), (1,1), (1,2)...
            # 1st Sqaure -> (0,3), (0,4), (0,5),(1,3), (1,4), (1,5)...
            # 2nd Square -> (0,6), (0,7), (0,8), (1,6), (1,7)....
            # use i to represent x coord and j to represent y coord
            seenSquare = set()
            for i in range(3): # done to build the three by three square
                for j in range(3):
                    # squares 0,1,2 -> x coords: 0, 1, 2. 0//3 = 0 (floor division)
                    # squares 3,4,5 -> x coords: 3, 4, 5. (3//3 = 1, 4//3 = 1, 5//3 = 1)
                    # squares 6,7,8 -> x coords: 6, 7, 8. 6//3 = 2 * 3 + 0 = 6, 7//3 = 2 * 3 + 1 = 7,
                    row = (num // 3) * 3 + i 
                    # squares 0,3,6 -> y coords: 0, 1, 2. 0 % 3 = 0, 3 % 3 = 0,
                    # squares 1,4,7 -> y coords: 3, 4, 5. 1 % 3 = (1 * 3) + j(0) = 3, 4//3 = 1 * 3 + j (1) = 4 ....
                    # squares 2,5,8 -> % 3 = 2. y coords: 6,7,8 = 2 * 3 + 0 = 6, 2 * 3 + 1 = 7 .... 
                    col = (num % 3) * 3 + j

                    if board[row][col] != ".": 
                        if board[row][col] in seenSquare: 
                            return False
                        seenSquare.add(board[row][col])
                
        return True
        