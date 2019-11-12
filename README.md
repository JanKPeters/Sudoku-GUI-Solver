# Sudoku-GUI-Solver
This is a sudoku solver using the backtracking algorithm. It includes a graphical GUI as well as a text based version.

Run GUI.py to play sudoku.

# Instructions
Click a box and hit the number on your keybaord to pencil in a number. To confirm that value press the ENTER key on that box. To delete a pencil in you can click DEL. Finally to solve the board press SPACE, sit back and watch the algorithm run.
Press n to generate a new puzzle.

# Puzzle generator
In addition to the original solver "See video tutorial from TechwithTim" the gui now generates a random sudoku at start up.
When the Gui is loaded just press n key on the keyboard to generate a new sudoku puzzle and reset the game.

! This generator is still a simple algorithm and does generate solvable puzzles but not necessarily unique puzzles. It does not check for unique rectangles "yet" ! Still fun though.
A common way as far as I know, would be to use a solver (backtracker for example) to check if there are more than one possible solutions, however that will slow the generation down significantly.
The task is therefore to find an algorithm that can check/ensure uniqueness without checking every single solution.

# Video Tutorial

You can view the video tutorials on how to create this project here: https://www.youtube.com/watch?v=eqUwSA0xI-s&t=871s

# Run in Gitpod

You can also run Sudoku-GUI-Solver in Gitpod, a free online dev environment for GitHub:

If you're intersted in a paid subscription with GitPod use the coupon code: TECHWITHTIM2FQBMX

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/techwithtim/Sudoku-GUI-Solver/blob/master/GUI.py)
