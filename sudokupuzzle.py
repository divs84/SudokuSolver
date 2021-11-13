from typing import List

class SudokuPuzzle:
    
    def __init__(self, puzzle: List):
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


    def is_valid_spot(self, value: int, row: int, column: int) -> bool:
        """
        Check if a specific spot within a given Sudoku puzzle
        is valid.

        Keyword arguments:
        value  -- the value (0-9) to validate in the specific Sudoku cell
        row    -- the row of the Sudoku cell to validate
        column -- the column of the Sudoku cell to validate
        """
        squareX = column - (column % 3)
        squareY = row - (row % 3)

        # Check all cells in the row for a duplicate
        for x in range(0, 9):
            if self.solved_puzzle[row][x] == value:
                return False
        
        # Check all cells in the column for a duplicate
        for y in range(0, 9):
            if self.solved_puzzle[y][column] == value:
                return False

        # Check all cells in the 3x3 square for a duplicate
        for sX in range(squareX, squareX+3):
            for sY in range(squareY, squareY+3):
                if self.solved_puzzle[sY][sX] == value:
                    return False

        return True


    def solve(self):
        """
        Solve a given Sudoku puzzle.

        """
        
        for x in range(0, 9):
            for y in range (0, 9):
                if self.solved_puzzle[y][x] == 0:
                    for val in range(1, 10):
                        if self.is_valid_spot(val, y, x):
                            self.solved_puzzle[y][x] = val
                            if self.solve():
                                return True
                            else:
                                self.solved_puzzle[y][x] = 0
                    return False
        return True