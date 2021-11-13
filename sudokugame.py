import getopt
import numpy as np
from sudokupuzzle import SudokuPuzzle
from sudokusolver import SudokuSolver
import sys

class SudokuGame:

    def __init__(self, argv):
        
        puzzle_file = ""

        try:
            opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        except getopt.GetoptError:
            self.display_help()
            sys.exit(2)

        if len(opts) == 0:
            self.display_help()
            sys.exit()

        for opt, arg in opts:
            if opt == '-h':
                self.display_help()
                sys.exit()
            elif opt in ("-i", "--ifile"):
                puzzle_file = arg.strip()
            else:
                self.display_help()
                sys.exit() 

        puzzle = SudokuPuzzle(self.load_from_file(puzzle_file))

        self.sudokusolver = SudokuSolver(puzzle)
        
        print(f"\nPUZZLE\n{self.sudokusolver}\n")
        
        
    def load_from_file(self, puzzle_file):
        """
        Load a Sudoku puzzle from a given filename
        and parse into a 9x9 2D array

        Keyword arguments:
        puzzle_file -- the file containing the Sudoku file
        """
        #puzzle = [[0]*9]*9
        puzzle = []

        f = open(puzzle_file, "r")

        for i in range(0,9):
            row = f.readline().strip().split(",")[0:9]
            puzzle.append([int(i) for i in row])
        
        return puzzle

    
    def complete_puzzle(self):
        if self.sudokusolver.solve():
            print(f"\nSOLVED PUZZLE\n{self.sudokusolver}\n")
        else:
            print("\n\nPUZZLE IS UNSOLVEABLE :(")

    def display_help(self):
        print("usage: sudokugame.py -i <puzzlefile>")
        print("\t-i <puzzlefile>: a comma-separated text file containing a Sudoku puzzle.")
        print("\tZero (0) must be used in the puzzlefile to indicate a blank spot in the puzzle.")

if __name__ == "__main__":
    game = SudokuGame(sys.argv[1:])
    game.complete_puzzle()