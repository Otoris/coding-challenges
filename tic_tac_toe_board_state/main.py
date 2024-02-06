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
    

if __name__ == "__main__":
    main()

