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
    """
    Vérifie si le joueur a gagné en vérifiant les lignes, colonnes et diagonales.
    """
    
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
