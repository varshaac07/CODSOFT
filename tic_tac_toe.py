import math

# Initialize board
board = [" " for _ in range(9)]

# Display board
def print_board():
    print()
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")
    print()

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    best_move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

# Player move
def player_move():
    try:
        move = int(input("Enter position (1-9): ")) - 1
        if board[move] == " ":
            board[move] = "X"
        else:
            print("Invalid move! Try again.")
            player_move()
    except:
        print("Enter a number between 1 and 9.")
        player_move()

# Main game
def play_game():
    print("=== Tic Tac Toe ===")
    print("You are X | AI is O")
    print("Positions: 1 to 9\n")

    while True:
        print_board()
        player_move()

        if check_winner("X"):
            print_board()
            print("🎉 You win!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move()

        if check_winner("O"):
            print_board()
            print("🤖 AI wins!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

# Run game
if __name__ == "__main__":
    play_game()