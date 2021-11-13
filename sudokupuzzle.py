from typing import List

class SudokuPuzzle:
    
    def __init__(self, puzzle):
        self.original_puzzle = puzzle.copy()
        self.solved_puzzle = puzzle.copy()


    def __str__(self):
        strs = ""
        for y in range(0, 9):
            if y % 3 == 0:
                strs += "-" * 25 + "\n"
            row = ""
            for x in range(0, 9):
                if x % 3 == 0:
                    row += "| "
                if self.solved_puzzle[y][x] == 0:
                    row += f"{'':<2}"
                else:
                    row += f"{self.solved_puzzle[y][x]:<2}"
            strs += row + "|\n"
        strs += "-" * 25

        return strs
