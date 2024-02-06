# Tic Tac Toe Game State Analyzer

Skip to [Results](#results) and [Setup](#setup)

## Objective
Write a program that analyzes the state of a Tic Tac Toe board and returns the game's current state. The board state will be provided as an input string.

**Input Format**
The input string represents the Tic Tac Toe board's rows, from top to bottom, with each cell separated by commas. The board can contain the characters X, O, and blanks (represented by ''). The input can be case-insensitive.

Example: `"x,o,x,o,x,o,x,o,x"`

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

## Input Constraints
The input will always be a string.

## Results

Test cases are passing

![Test cases are passing](https://i.imgur.com/5iFihGG.png)

Coverage report

```bash
Name                                   Stmts   Miss  Cover
----------------------------------------------------------
tic_tac_toe_board_state\main.py           28      0   100%
tic_tac_toe_board_state\test_main.py      51      0   100%
----------------------------------------------------------
TOTAL                                     79      0   100%
```

## Setup

Notes: Tested with Python 3.10 on Windows 11


1. Clone the repository
2. Navigate to the project directory
3. Setup the virtual environment
```bash
python -m venv venv
```
4. Activate the virtual environment
```bash
source venv/bin/activate
```
5. Install the requirements
```bash
pip install -r requirements.txt
```
6. Configure and run the tests in your VSCode
7. Or run the tests in the terminal
```bash
pytest
```
8. For code coverage
```bash
coverage run -m pytest
coverage report
```
