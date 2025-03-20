"""Instructions

The game is played on a grid that’s 3 squares by 3 squares.
Players take turns putting their marks (O or X) in empty squares.
The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.


Hint

To do this project, you basically need to create four functions:

display_board() – To display the Tic Tac Toe board (GUI).
player_input(player) – To get the position from the player.
check_win() – To check whether there is a winner or not.
play() – The main function, which calls all the functions created above.
Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want."""



def display_board(board):

    print("Welcome to Tic Tac Toe !")
    print("TIC TAC TOE")
    print()
    print("*" * 17)
    for row in range(3):
        print("*    |   |    *")
        print(f"*  {board[row][0]} | {board[row][1]} | {board[row][2]}  *")
        print("*    |   |    *")
        if row < 2:
            print("* ---|---|--- *")
    print("*" * 17)



def player_input(board, player):

    while True:
        try:
            print(f"\nPlayer {player}'s turn...")
            row = int(input("Enter row (1,2,3): ")) - 1  
            col = int(input("Enter column (1,2,3): ")) - 1

            if row in [0, 1, 2] and col in [0, 1, 2]:
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Position already taken. Try again.\n")
            else:
                print("Invalid row or column. Try again.\n")
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")
    return board



def check_win(board, player):
    
    
    for row in board:
        if all([spot == player for spot in row]):
            return True

    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False



def check_null(board):
   
    for row in board:
        if " " in row:
            return False
    return True



def play():
    
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

   
    while not game_over:
        display_board(board)
        player_input(board, current_player)
        
        
        if check_win(board, current_player):
            display_board(board)
            print(f"\nFélicitations, le joueur {current_player} a gagné !")
            game_over = True
        
        elif check_null(board):
            display_board(board)
            print("\nMatch nul !")
            game_over = True
        else:
            
            current_player = "O" if current_player == "X" else "X"




if __name__ == '__main__':
    play()
