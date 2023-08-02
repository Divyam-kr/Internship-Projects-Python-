board = ["-" , "-" , "-" ,
         "-" , "-" , "-" ,
         "-" , "-" , "-"]

currentPlayer = "O"
winner = None
gameRunning = True

player_1 = input("Enter the name of Player 1 :")
player_2 = input("Enter the name of Player 2 :")
print()
print(player_1 , " will go with X and " , player_2 , " will go with O")
print()

#printing the game board
def printBoard (board):
    
    print (board [0]  + "    |    " + board [1] + "    |    " + board [2] )
    print("-------------------- ")
    print (board [3] + "    |    " + board [4] + "    |    " + board [5])
    print("-------------------- ")
    print (board [6] + "    |    " + board [7] + "    |    " + board [8])
    
    
    
    
#Taking input from the players

def playerInput (board):
    inp = int(input("Enter a number 1-9:"))
    if inp >= 1 and inp <= 9 and board [inp-1] == "-":
        board [inp-1] = currentPlayer
        return 0
    else:
        print("\nOops that spot is already occupied!")
        return 1
        
#checkingg horizontally        
def checkHorizontle (board):
    global winner
    if board [0] == board [1] ==board [2] and board [1] != "-":
        winner = board [0]
        return True
    elif board [3] == board [4]== board [5] and board [3] != "-":
        winner = board [3]
        return True
    elif board [6] == board [7] == board [8] and board [6] != "-":
        winner = board [6]
        return True

#Checking Vertically
def checkVertical (board):
    global winner
    if board [0]==board [3] == board [6] and board [0] != "-":
        winner = board [0]
        return True
    elif board [1] == board [4] == board [7] and board [1] != "-":
        winner = board [1]
        return True
    elif board [2] == board [5] == board [8] and board [2] != "-":
        winner = board [2]
        return True

#Checking Diagonally
def checkDiag (board):
    global winner
    if board [0]==board [4]== board [8] and board [0] != "-":
        winner = board [0]
        return True
    elif board [2] == board [4]== board [6] and board [2] != "-":
        winner = board [2]
        return True
#Tie condition
def checkTie(board):
    global gameRunning
    if "-" not in board:
        print()
        printBoard (board)
        print("\n\n The match between ", player_1 , "and" , player_2 , " is tied !!")
        gameRunning = False

        
#Winner or Loser
def checkWin():
    global gameRunning
    if checkDiag (board) or checkHorizontle(board) or checkVertical (board):
        print()
        printBoard(board)
        print("")
        if winner=="X":
            print (f"THE WINNER IS {player_1}")
        if winner=="O":
            print (f"THE WINNER IS {player_2}")
        print("")    
        gameRunning=False
        

        
#For switching the players
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
        print()
        print(player_2,"turn")
    else:
        currentPlayer = "X"
        print()
        print(player_1,"turn")
        
l = 0  
#Main        
while gameRunning==True:
    if l==0:
        switchPlayer()
    printBoard(board)
    l = playerInput(board)
    checkWin()
    checkTie(board)