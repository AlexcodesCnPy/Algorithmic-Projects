board = [[7, 8, 0, 4, 0, 0, 1, 2, 0], 
		 [6, 0, 0, 0, 7, 5, 0, 0, 9], 
		 [0, 0, 0, 6, 0, 1, 0, 7, 8], 
		 [0, 0, 7, 0, 4, 0, 2, 6, 0], 
		 [0, 0, 1, 0, 5, 0, 9, 3, 0], 
		 [9, 0, 4, 0, 6, 0, 0, 0, 5], 
		 [0, 7, 0, 3, 0, 0, 0, 1, 2], 
		 [1, 2, 0, 0, 0, 7, 4, 0, 0], 
		 [0, 4, 9, 2, 0, 6, 0, 0, 7]]

#empty cell
def find_(bo):
	for i in range(9):
		for j in range(9):
			if bo[i][j] == 0:
				return (i,j)

	return False

#validate
def validate(bo,n,row,col):
	if n in bo[row]:
		return False

	if n in [bo[k][col] for k in range(9)]:
		return False

	else:
		x = (row // 3)*3
		y = (col // 3)*3
		for r in range(x,x+3):
			for c in range(y,y+3):
				if bo[r][c] == n:
					return False

	return True

#solve
def solve(bo):
	find = find_(bo)
	if not find:
		return True

	else:
		row,col = find


	for n in range(1,10):
		if validate(bo,n,row,col):
			bo[row][col] = n

			if solve(bo):
				return True

			bo[row][col] = 0


	return False



d = solve(board)
print(matrix(board))