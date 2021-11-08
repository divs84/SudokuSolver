import getopt
import numpy as np
import sys

def display_puzzle(puzzle, orig_puzzle=None):
    """
    Display a given Sudoku puzzle to the console.

    Keyword arguments:
    puzzle -- the 9x9 2D array containing the puzzle
    """

    print("-" * 37)
    for y in range(0, 9):
        for x in range(0, 9):
            if puzzle[y, x] == 0:
                print("|   ", end='')
            else:
                if not orig_puzzle is None and orig_puzzle[y, x] != 0:
                    print(f"| \033[1m\033[95m{puzzle[y, x]}\033[0m ", end='')
                else:
                    print(f"| {puzzle[y, x]} ", end='')
        print("|\n" + "-" * 37)


def load_from_file(puzzle, puzzle_file="puzzle.txt"):
    """
    Load a Sudoku puzzle from a given filename
    and parse into a 9x9 2D array

    Keyword arguments:
    puzzle_file -- the file containing the Sudoku file
    """
    f = open(puzzle_file, "r")

    for i in range(0,9):
        row = f.readline().strip().split(",")[0:9]
        puzzle[i] = row

    print(f"PUZZLE LOADED FROM FILE {puzzle_file}")
    display_puzzle(puzzle)
    
    return puzzle


def is_valid_spot(puzzle, value, row, column):
    """
    Check if a specific spot within a given Sudoku puzzle
    is valid.

    Keyword arguments:
    puzzle -- the 9x9 2D array containing the puzzle
    value  -- the value (0-9) to validate in the specific Sudoku cell
    row    -- the row of the Sudoku cell to validate
    column -- the column of the Sudoku cell to validate
    """
    squareX = column - (column % 3)
    squareY = row - (row % 3)

    # Check all cells in the row for a duplicate
    for x in range(0, 9):
        if puzzle[row, x] == value:
            return False
    
    # Check all cells in the column for a duplicate
    for y in range(0, 9):
        if puzzle[y, column] == value:
            return False

    # Check all cells in the 3x3 square for a duplicate
    for sX in range(squareX, squareX+3):
        for sY in range(squareY, squareY+3):
            if puzzle[sY, sX] == value:
                return False

    return True


def solve_puzzle(puzzle):
    """
    Solve a given Sudoku puzzle.

    Keyword arguments:
    puzzle -- the 9x9 2D array containing the puzzle
    """

    for x in range(0, 9):
        for y in range (0, 9):
            if puzzle[y, x] == 0:
                for val in range(1, 10):
                    print(f"Testing row {x}, col {y} with value {val}\r", end="")
                    if is_valid_spot(puzzle, val, y, x):
                        puzzle[y, x] = val
                        if solve_puzzle(puzzle):
                            return True
                        else:
                            puzzle[y, x] = 0
                return False
    return True


def main(argv):
    puzzle = np.zeros((9,9), dtype='int16')

    puzzle_file = ""

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print("SudokuSolver.py -i <puzzlefile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("SudokuSolver.py -i <puzzlefile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            puzzle_file = arg

    #load_from_file(puzzle)
    #load_from_file(puzzle, puzzle_file="puzzle1.txt")
    load_from_file(puzzle, puzzle_file)
    
    solved_puzzle = np.copy(puzzle)
    
    if solve_puzzle(solved_puzzle):
        print("\n\nSOLVED PUZZLE")
        display_puzzle(solved_puzzle, puzzle)
    else:
        print("\n\nPUZZLE IS UNSOLVEABLE :(")

if __name__ == "__main__":
    main(sys.argv[1:])