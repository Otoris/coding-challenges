def main(state: str):
    state = state.lower().split(",")
    # Check for invalid length
    if len(state) != 9:
        return "Error: Invalid input"
    
    #Check for invalid characters
    if any(char not in 'xo' for char in state):
        print(state)
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
        ]

        for row in winning_boards:
            if row.count(player) == 3:
                return True
            else:
                return False
            
    x_winner = check_winner('x')
    o_winner = check_winner('o')

    if x_winner:
        return "X-winner"
    elif o_winner:
        return "O-winner"
    else:
        return "Incomplete"


if __name__ == "__main__":
    main()

