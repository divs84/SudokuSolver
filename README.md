# SudokuSolver
A python CLI program that can read a Sudoku puzzle from a file and solve it using recursive backtracking.

## Usage
```bash
python sudokusolver.py -i <puzzlefile>
```

## Puzzle File
The program expects the puzzle file in a specific format to work properly:
    - All values are comma-separated.
    - One line in the file corresponds to one row in the puzzle.
    - Must have exactly 9 comma-separated values on each line, and 9 lines in the file.
    - Any blank cells in the puzzle are to be filled in with a zero (0).

Here is an example layout of a puzzle following the rules described above:
```bash
5,3,0,0,7,0,0,0,0
6,0,0,1,9,5,0,0,0
0,9,8,0,0,0,0,6,0
8,0,0,0,6,0,0,0,3
4,0,0,8,0,3,0,0,1
7,0,0,0,2,0,0,0,6
0,6,0,0,0,0,2,8,0
0,0,0,4,1,9,0,0,5
0,0,0,0,8,0,0,7,9
```

Additional example puzzle files can be found in the __puzzles__ folder of this project.