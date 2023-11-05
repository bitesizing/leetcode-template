"""https://leetcode.com/problems/valid-sudoku/
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""

from typing import List
import math

class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		rows, cols, boxes = [], [], []
		for i in range(9):
			rows.append(set())
			cols.append(set())
			boxes.append(set())
        
		for row in range(9):
			for col in range(9):
				square = board[row][col]
				if square == ".": continue
				
				box = 3*math.floor(row/3) + math.floor(col/3)
				print(f"square={square}, row={row}, col={col}, box={box}")

				if square in boxes[box] or square in rows[row] or square in cols[col]:
					return False
				else:
					boxes[box].add(square)
					cols[col].add(square)
					rows[row].add(square)
		return True

board = [["5","3",".",".","7",".",".",".","."]
		,["6",".",".","1","9","5",".",".","."]
		,[".","9","8",".",".",".",".","6","."]
		,["8",".",".",".","6",".",".",".","3"]
		,["4",".",".","8",".","3",".",".","1"]
		,["7",".",".",".","2",".",".",".","6"]
		,[".","6",".",".",".",".","2","8","."]
		,[".",".",".","4","1","9",".",".","5"]
		,[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))

