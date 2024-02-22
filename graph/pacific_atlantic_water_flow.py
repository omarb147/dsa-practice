
from typing import List

# ---------------------------------- Problem --------------------------------- #
# URL:https://leetcode.com/problems/pacific-atlantic-water-flow/
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
# The Pacific Ocean touches the island's left and top edges, 
# and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. 
# You are given an m x n integer matrix heights where heights[r][c] 
# represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, 
# south, east, and west if the neighboring cell's height is less than or equal to 
# the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that 
# rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# ----------------------------------- Notes ---------------------------------- #
# need locations of the oceans -> pacific -> left + top , altantic -> right + bottom 
# dfs from each position to both boundaries 
# end search if a cell can't flow in any given direction 
# need to capture the cordinates of the start of the DFS and that's the return

# --------------------------------- Solution --------------------------------- #
def pacificAtlantic_dfs(self, heights: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(heights), len(heights[0])
    direction_deltas = [(0,1),(-1,0),(0,-1),(1,0)]

    pacific_reachable = set()
    atlantic_reachable = set()

    def is_valid(row, col, seen):
        return 0 <= row < ROWS and 0 <= col < COLS and (row,col) not in seen


    def dfs(row, col, reachable):
        if is_valid(row,col, reachable):
            print((row,col))
            reachable.add((row,col))
            curr_height = heights[row][col]

            for row_delta, col_delta in direction_deltas:
                r,c = row+row_delta, col+col_delta

                if is_valid(r,c, reachable) and heights[r][c] >= curr_height:
                    dfs(r,c,reachable)
        

    for col in range(COLS):
        dfs(0,col, pacific_reachable)
        dfs(ROWS-1,col, atlantic_reachable)
    for row in range(ROWS):
        dfs(row, 0, pacific_reachable)
        dfs(row, COLS-1, atlantic_reachable)

    return list(atlantic_reachable & pacific_reachable)

# TODO - BFS Approach