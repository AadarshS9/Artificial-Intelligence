def attack(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return True
    
    # Check upper diagonal on left side
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return True

    # Check upper diagonal on right side
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return True

    return False

def placing_queens(chessboard,row,n):
  if row==n:
    return True #queens placed at non-attacking position so exit
  
  for col in range(n):
    if not attack(chessboard,row,col,n):
      chessboard[row][col]=1 #place queen if cell empty and attack is false

      if placing_queens(chessboard,row+1,n):
        return True #else read next cell

      chessboard[row][col]=0 #mark as visited
  
  return False

n=int(input("Kindly enter the number of queens to be placed: "))
chessboard=[[0 for _ in range(n)]for _ in range(n)]

if placing_queens(chessboard, 0, n):
  print("\nQueens successfully placed at non-attacking positions:")
  for i, row in enumerate(chessboard):
    for col in chessboard[i]:
        print(col,end='\t')
    print('\n')
else:
  print("Solution does not exist for this configuration.")
