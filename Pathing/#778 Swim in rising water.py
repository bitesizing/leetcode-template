"""You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0)."""

# %%
from icecream import ic
from typing import List
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def calc_square(curr_idx, old_idx):
            """ Recurse for each individual square. """
            row, col = curr_idx
            old_row, old_col = old_idx
            original = grid[row][col]
            new = grid[old_row][old_col][0]

            if isinstance(original, tuple):  # if we've visited before
                current, original = original
                new = min(current, new)
                grid[row][col] = (max(original, new), original)

            else:  # if first time visiting
                grid[row][col] = (max(original, new), original)
                if row+1<n_row: queue.append(((row+1, col), (curr_idx)))
                if col+1<n_col: queue.append(((row, col+1), (curr_idx)))


        grid[0][0] = (grid[0][0], grid[0][0])
        # heap format = (t_value, new_idx, old_idx)
        heap = [(0, (0,1),(0,0)), (0, (1,0),(0,0))]  # might be a way to ditch this, works for now?
        n_row = len(grid)
        n_col = len(grid[0])

        while queue:
            print(queue[0])
            curr_idx, old_idx = queue.popleft()
            calc_square(curr_idx, old_idx)
        return grid[-1][-1][0]

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(Solution().swimInWater(grid))

# %%
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Go right and down
        # Add to min-queue to calculate which one you do next
        #
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(Solution().swimInWater(grid))