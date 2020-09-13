
# Initial Board

board=[[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]

# Entering the details that is default filled numbers

def fillDetails(board):
    try:
        while True:
            command=input("Enter 'y' to continue 'n' to stop\n").lower()
            if command=='y':
                num_list=list(map(int,input("Enter row,coloumn and number seperated by space respectively\n").split()))
                board[num_list[0]-1][num_list[1]-1]=num_list[2]
            elif command=='n':
                break

    except:
        fillDetails(board)


# Getting length of arrays 


board_len=len(board)
each_row_len=len(board[0])


# Printing Board in the specified manner of SUDOKU

def printBoard(board):
    for i in range(board_len):
        if i%3==0:
            print(" -----------------------")

        for j in range(each_row_len):
            if j%3==0:
                print("| ",end="")
            if j==8:
                print(board[i][j],end=" | \n")
            else:
                print(board[i][j],end=" ")
    print(" -----------------------")
    

# Check if a place in SUDOKU is empty or not

def findEmpty(board):
    for i in range(board_len):
        for j in range(each_row_len):
            if board[i][j]==0:
                return (i,j)
    return None


# Validating the empty place
'''
A place is valid only if that number is not repeted in
1) That row
2) That column
3) That 3*3 box
as per SUDOKU Rule

'''
def checkValid(board,num,pos):
    # To check the number in row
    for i in range(each_row_len):
        if board[pos[0]][i]==num:
            return False
    
    # To check the number in column
    for j in range(board_len):
        if board[j][pos[1]]==num:
            return False

    # To check the 3*3 box

    # First make them 9 parts
    pos_x = pos[0]//3
    pos_y = pos[1]//3

    for i in range(pos_x*3,pos_x*3+3):
        for j in range(pos_y*3,pos_y*3+3):
            if board[i][j]==num:
                return False

    return True

# Solving the SUDOKU

def solve(board):
    # If not find empty then return True which will end the work
    find = findEmpty(board)
    if find:
        row,col=find
    else:
        return True
    
    for i in range(1,10):
        # If valid then put that number else put 0
        if checkValid(board,i,(row,col)):
            board[row][col]=i
            
            if solve(board)==True:
                return True 
            else:
                solve(board)
        else:
            board[row][col]=0

# Main Function

if __name__ == "__main__":
    print("Welcome to SUDOKU solver !")
    fillDetails(board)
    print("\n Your Problem SUDOKU is \n")
    printBoard(board)
    print("\n Your Solved SUDOKU is \n")
    solve(board)
    printBoard(board)