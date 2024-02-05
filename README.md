# Tic Tac Toe Game State Analyzer
## Objective
Write a program that analyzes the state of a Tic Tac Toe board and returns the game's current state. The board state will be provided as an input string.

**Input Format**
The input string represents the Tic Tac Toe board's rows, from top to bottom, with each cell separated by commas. The board can contain the characters X, O, and blanks (represented by ''). The input can be case-insensitive.

Example: `"X,O,X,O,X,O,X,O,X"`

## Requirements
Your program should validate the input and then determine the game's state. The possible return strings are as follows:

"Tie": The game is over with no winner.
"Incomplete": The game is still in progress.
"X-winner": Player X has won the game.
"O-winner": Player O has won the game.
"Error": The input is invalid. This could be due to an incorrect number of plays (e.g., too many plays by one player without the other) or the presence of two winners.

## Rules
- The game is played on a 3x3 grid.
- X and O players take turns putting their marks in empty squares.
- Either X or O can start the game.
- The first player to achieve a line of three of their marks (vertically, horizontally, or diagonally) is the winner.
- If all 9 squares are filled and no player has three marks in a line, the game is considered a tie.

## Testing
Include test cases covering all possible outcomes and edge cases, such as:

- A valid game with a winner.
- A tie game with no blank spaces left.
- An incomplete game.
- An invalid game state due to rule violations.
- An invalid input format.