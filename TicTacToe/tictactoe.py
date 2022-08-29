Board = ['-','-','-',
         '-','-','-',
         '-','-','-']

# Checks if game is over or not
GameStillGoingOn = True

# decides who is the winner
Winner = None

# assigning the player initially
Current_Player = 'X'    

# function from where the game actually starts
def Play_Game():
    DisplayBoard()

    while GameStillGoingOn:
        Turn(Current_Player)
        IsGameOver()
        FlipPlayer()
    
    if Winner == 'X' or Winner == 'O':
        print(Winner + " WON!!!")
    elif Winner == None:
        print("Match Tied!!!")

# function to display the board
def DisplayBoard():
    print('\n')
    print(Board[0] + " | " + Board[1] + " | " + Board[2] + "    1 | 2 | 3")
    print(Board[3] + " | " + Board[4] + " | " + Board[5] + "    4 | 5 | 6")
    print(Board[6] + " | " + Board[7] + " | " + Board[8] + "    7 | 8 | 9")
    print('\n')

# specific player's turn 
def Turn(Player):
    print(Player+"'s turn")
    position = input("Choose position between 1 - 9: ")

    valid = False
    while not valid:
        while position not in ['1','2','3','4','5','6','7','8','9']: # if user enters value that excludes those in list
            position = input("Choose position between 1 - 9: ")
        position = int(position) - 1
        if Board[position] == "-":
            valid = True
        else:
            print("You can't go there. Try another place.")
    Board[position] = Player
    DisplayBoard()

# function to check if the game is over or not
def IsGameOver():
    WhoIsWinner()
    GameTie()

# function to decide who is winner
def WhoIsWinner():
    global Winner

    RowWinner = CheckRows()
    ColumnWinner = CheckColumns()
    DiagonalWinner = CheckDiagonals()

    if RowWinner:
        Winner = RowWinner
    elif ColumnWinner:
        Winner = ColumnWinner
    elif DiagonalWinner:
        Winner = DiagonalWinner
    else:
        Winner = None

# function to check all rows
def CheckRows():
    global GameStillGoingOn

    FirstRow = Board[0] == Board[1] == Board[2] != '-'
    SecondRow = Board[3] == Board[4] == Board[5] != '-'
    ThirdRow = Board[6] == Board[7] == Board[8] != '-'

    if FirstRow or SecondRow or ThirdRow:
        GameStillGoingOn = False
    if FirstRow:
        return Board[0]
    elif SecondRow:
        return Board[3]
    elif ThirdRow:
        return Board[6]
    else:
        return None

# function to check all columns
def CheckColumns():
    global GameStillGoingOn

    FirstCol = Board[0] == Board[3] == Board[6] != '-'
    SecondCol = Board[1] == Board[4] == Board[7] != '-'
    ThirdCol = Board[2] == Board[5] == Board[8] != '-'

    if FirstCol or SecondCol or ThirdCol:
        GameStillGoingOn = False
    if FirstCol:
        return Board[0]
    elif SecondCol:
        return Board[1]
    elif ThirdCol:
        return Board[2]
    else:
        return None

# function to check all diagonals
def CheckDiagonals():
    global GameStillGoingOn

    FirstDiagonal = Board[0] == Board[4] == Board[8] != '-'
    SecondDiagonal = Board[2] == Board[4] == Board[6] != '-'

    if FirstDiagonal or SecondDiagonal:
        GameStillGoingOn = False
    if FirstDiagonal:
        return Board[0]
    elif SecondDiagonal:
        return Board[2]
    else:
        return None

# function to check if the game tied
def GameTie():
    global GameStillGoingOn
    if "-" not in Board:
        GameStillGoingOn = False
        return True
    else:
        return False

# flip the player
def FlipPlayer():
    global Current_Player

    if Current_Player == 'X':
        Current_Player = 'O'
    elif Current_Player == 'O':
        Current_Player = 'X'

# main function
def main():
    #print("1. Play\n2. Exit")
    #choice = input("Enter the choice: ")
    #match choice:
     #   case 1:
    Play_Game()
      #  case 2:
       #     exit
# call to main function
if __name__ == "__main__":
    main()