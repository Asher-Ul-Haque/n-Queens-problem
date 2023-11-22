print('THIS IS THE COMMAND LINE SOLVER FOR N-QUEENS BACKTRACKING PROBLEM')

def makeBoard():
    # Get the number of queens from the user
    n = int(input("Enter the number of queens: "))
    # Create a board of size n x n
    board = [[0 for x in range(n)] for y in range(n)]
    return board

def printBoard(board):
    # Print the board
    print('The board is: ')
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' | ')
        print()
        print('- ' * len(board)*2)


def isSafe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check if there is a queen in the upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check if there is a queen in the lower left diagonal
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True
board=makeBoard()

def solve(col=0):
    global board
    printBoard(board)
    input()
    # Check if all queens are placed
    print(len(board))
    if col>=len(board):
        return True
    # Check for each row in the current column
    for i in range(len(board)):
        # Check if the current position is safe
        if isSafe(board, i, col):
            # Place the queen in the current position
            board[i][col] = 1
            # Check if the next queen can be placed
            if solve(col+1):
                return True
            # If the next queen cannot be placed, backtrack
            board[i][col] = 0
    return False

printBoard(board)
solve()
printBoard(board)
