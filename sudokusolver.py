import getopt
from sudokupuzzle import SudokuPuzzle
import sys

class SudokuSolver:

    def __init__(self, puzzle_file):
        self.sudokupuzzle = SudokuPuzzle(self.load_from_file(puzzle_file))
        print(f"\nPUZZLE\n{self.sudokupuzzle}\n")


    def load_from_file(self, puzzle_file: str):
        """
        Load a Sudoku puzzle from a given filename
        and parse into a 9x9 2D array

        Keyword arguments:
        puzzle_file -- the filename containing the Sudoku file
        """
        puzzle = []

        f = open(puzzle_file, "r")

        for i in range(0,9):
            row = f.readline().strip().split(",")[0:9]
            puzzle.append([int(i) for i in row])
        
        return puzzle

    
    def complete_puzzle(self):
        if self.sudokupuzzle.solve():
            print(f"\nSOLVED PUZZLE\n{self.sudokupuzzle}\n")
        else:
            print("\nPUZZLE IS UNSOLVEABLE :(")


    @staticmethod
    def display_help():
        print("usage: python sudokusolver.py -i <puzzlefile>")
        print("\t-i <puzzlefile>: a comma-separated text file containing a Sudoku puzzle.")
        print("\tZero (0) must be used in the puzzlefile to indicate a blank spot in the puzzle.")


if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        SudokuSolver.display_help()
        sys.exit(2)

    if len(opts) == 0:
        SudokuSolver.display_help()
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            SudokuSolver.display_help()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            puzzle_file = arg.strip()
        else:
            SudokuSolver.display_help()
            sys.exit() 

    sudoku = SudokuSolver(puzzle_file)
    sudoku.complete_puzzle()


