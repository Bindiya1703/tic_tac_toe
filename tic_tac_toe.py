import math
board = [' ' for _ in range(9)]  
player = 'X'
ai = 'O'
def print_board():
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
def check_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return [player, player, player] in win_conditions
def check_draw(board):
    return ' ' not in board
def minimax(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, ai):
        return 1
    elif check_winner(board, player):
        return -1
    elif check_draw(board):
        return 0
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai
                eval = minimax(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = player
                eval = minimax(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            score = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move
def play_game():
    print_board()
    while True:
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] != ' ':
            print("Invalid move, try again.")
            continue
        board[human_move] = player
        if check_winner(board, player):
            print_board()
            print("You win!")
            break
        elif check_draw(board):
            print_board()
            print("It's a draw!")
            break
        ai_move = best_move()
        board[ai_move] = ai
        print_board()
        if check_winner(board, ai):
            print("AI wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
play_game()
