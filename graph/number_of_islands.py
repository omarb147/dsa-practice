# ---------------------------------- Problem --------------------------------- #
# URL : https://leetcode.com/problems/number-of-islands/
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.


# ----------------------------------- Notes ---------------------------------- #

# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "1"],
# ]
# start dfs from every position in the grid
# keep searching until we reach the edge
# at the edge add 1 on - then we have covered a whole island
# since all items are going into seen when we go to the next position to start dfs we get nothing


# --------------------------------- Solution --------------------------------- #
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    seen = set()
    direction_deltas = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    ans = 0

    def is_valid(row, col):
        return 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in seen

    def dfs(row, col):
        if is_valid(row, col) and grid[row][col] == "1":
            seen.add((row, col))

            for row_delta, col_delta in direction_deltas:
                dfs(row + row_delta, col + col_delta)

            if grid[row][col] == "1":
                return 1
        return 0

    for row in range(ROWS):
        for col in range(COLS):
            ans += dfs(row, col)

    return ans


print(numIslands(grid))
