import numpy as np

class sudoku:
    def __init__(self,board):
        self.board = board

    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return (r,c)


        return False


    def validate(self,n, row,col):
        if n in self.board[row]:
            return False

        if n in [self.board[k][col] for k in range(9)]:
            return False

        r = (row // 3)*3
        c = (col // 3)*3
        for k in range(r,r+3):
            for h in range(c,c+3):
                if n == self.board[k][h]:
                    return  False


        return True


    def solve(self):
        find = self.find_empty()
        if not find:
            return True

        else:
            row,col = find


        for n in range(1,10):
            if self.validate(n,row,col):
                self.board[row][col] = n

                if self.solve():
                    return True

                self.board[row][col] = 0


        return False



s = sudoku([[7, 8, 0, 4, 0, 0, 1, 2, 0], 
         [6, 0, 0, 0, 7, 5, 0, 0, 9], 
         [0, 0, 0, 6, 0, 1, 0, 7, 8], 
         [0, 0, 7, 0, 4, 0, 2, 6, 0], 
         [0, 0, 1, 0, 5, 0, 9, 3, 0], 
         [9, 0, 4, 0, 6, 0, 0, 0, 5], 
         [0, 7, 0, 3, 0, 0, 0, 1, 2], 
         [1, 2, 0, 0, 0, 7, 4, 0, 0], 
         [0, 4, 9, 2, 0, 6, 0, 0, 7]])

print(np.matrix(s.board))

d = s.solve()
print(d)

print(np.matrix(s.board))













