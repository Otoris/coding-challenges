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

**Remote setup** -> [Codesandbox Link](https://codesandbox.io/p/github/Otoris/coding-challenges/main?layout=%257B%2522sidebarPanel%2522%253A%2522EXPLORER%2522%252C%2522rootPanelGroup%2522%253A%257B%2522direction%2522%253A%2522horizontal%2522%252C%2522contentType%2522%253A%2522UNKNOWN%2522%252C%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522id%2522%253A%2522ROOT_LAYOUT%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522UNKNOWN%2522%252C%2522direction%2522%253A%2522vertical%2522%252C%2522id%2522%253A%2522clsafsyvo00063b6ftn3wnjq4%2522%252C%2522sizes%2522%253A%255B70%252C30%255D%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522EDITOR%2522%252C%2522direction%2522%253A%2522horizontal%2522%252C%2522id%2522%253A%2522EDITOR%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522EDITOR%2522%252C%2522id%2522%253A%2522clsafsyvo00023b6fkuc8lvaq%2522%257D%255D%257D%252C%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522SHELLS%2522%252C%2522direction%2522%253A%2522horizontal%2522%252C%2522id%2522%253A%2522SHELLS%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522SHELLS%2522%252C%2522id%2522%253A%2522clsafsyvo00043b6fcbf0cg8t%2522%257D%255D%252C%2522sizes%2522%253A%255B100%255D%257D%255D%257D%252C%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522DEVTOOLS%2522%252C%2522direction%2522%253A%2522vertical%2522%252C%2522id%2522%253A%2522DEVTOOLS%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522DEVTOOLS%2522%252C%2522id%2522%253A%2522clsafsyvo00053b6f3vd0hw4x%2522%257D%255D%252C%2522sizes%2522%253A%255B100%255D%257D%255D%252C%2522sizes%2522%253A%255B100%252C0%255D%257D%252C%2522tabbedPanels%2522%253A%257B%2522clsafsyvo00023b6fkuc8lvaq%2522%253A%257B%2522id%2522%253A%2522clsafsyvo00023b6fkuc8lvaq%2522%252C%2522tabs%2522%253A%255B%257B%2522type%2522%253A%2522FILE%2522%252C%2522filepath%2522%253A%2522%252Ftic_tac_toe_board_state%252Ftest_main.py%2522%252C%2522id%2522%253A%2522clsafxtl900ek3b6fq7qpbt2e%2522%252C%2522mode%2522%253A%2522temporary%2522%257D%255D%252C%2522activeTabId%2522%253A%2522clsafxtl900ek3b6fq7qpbt2e%2522%257D%252C%2522clsafsyvo00053b6f3vd0hw4x%2522%253A%257B%2522id%2522%253A%2522clsafsyvo00053b6f3vd0hw4x%2522%252C%2522tabs%2522%253A%255B%255D%257D%252C%2522clsafsyvo00043b6fcbf0cg8t%2522%253A%257B%2522id%2522%253A%2522clsafsyvo00043b6fcbf0cg8t%2522%252C%2522activeTabId%2522%253A%2522clsafxoym00bz3b6f6jx38swb%2522%252C%2522tabs%2522%253A%255B%257B%2522id%2522%253A%2522clsafsyvo00033b6fgzxsoey5%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522TERMINAL%2522%252C%2522shellId%2522%253A%2522clsafsza3000adkgu5dnn2ay6%2522%257D%252C%257B%2522type%2522%253A%2522TASK_LOG%2522%252C%2522taskId%2522%253A%2522CSB_RUN_OUTSIDE_CONTAINER%253D1%2520devcontainer%2520templates%2520apply%2520--template-id%2520%255C%2522ghcr.io%252Fdevcontainers%252Ftemplates%252Fpython%255C%2522%2520--template-args%2520%27%257B%257D%27%2520--features%2520%27%255B%255D%27%2522%252C%2522id%2522%253A%2522clsafv63n002c3b6frsyjsyqr%2522%252C%2522mode%2522%253A%2522permanent%2522%257D%252C%257B%2522type%2522%253A%2522TASK_LOG%2522%252C%2522taskId%2522%253A%2522pytest%2522%252C%2522id%2522%253A%2522clsafxoym00bz3b6f6jx38swb%2522%252C%2522mode%2522%253A%2522permanent%2522%257D%255D%257D%257D%252C%2522showDevtools%2522%253Afalse%252C%2522showShells%2522%253Atrue%252C%2522showSidebar%2522%253Atrue%252C%2522sidebarPanelSize%2522%253A15%257D)

**Local setup**
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
