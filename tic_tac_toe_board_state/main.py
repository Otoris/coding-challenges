def main(state: str):
    state = state.lower().split(",")
    # Check for invalid length
    if len(state) != 9:
        return "Error: Invalid input"
    
    # Check for invalid characters
    if any(char not in 'xo' for char in state):
        return "Error: Invalid input"
    
    # Validate turn counts
    x_count = state.count('x')
    o_count = state.count('o')
    if abs(x_count - o_count) > 1:
        return "Error: Invalid turn count"
    
    board = [state[:3], state[3:6], state[6:]]

    def check_winner(player):
        winning_boards = [
            [board[0][0], board[0][1], board[0][2]], # Horizontal top
            [board[1][0], board[1][1], board[1][2]], # Horizontal middle
            [board[2][0], board[2][1], board[2][2]], # Horizontal bottom
            [board[0][0], board[1][0], board[2][0]], # Vertical left
            [board[0][1], board[1][1], board[2][1]], # Vertical middle
            [board[0][2], board[1][2], board[2][2]], # Vertical right
            [board[0][0], board[1][1], board[2][2]], # Diagonal top left to bottom right
            [board[0][2], board[1][1], board[2][0]]  # Diagonal top right to bottom left
        ]

        for winning_board in winning_boards:
            # Check if all cells in the winning board are the same
            if all(cell == player for cell in winning_board):
                return True
        return False
    
    # Check for winners
    x_winner = check_winner('x')
    o_winner = check_winner('o')

    if x_winner and o_winner:
        return "Error: Two winners"
    elif x_winner:
        return "X-winner"
    elif o_winner:
        return "O-winner"
    # If we got here, and count total is not 9, then the game is incomplete
    elif x_count + o_count != 9:
        return "Incomplete"
    else:
        return "Tie"
