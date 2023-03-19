from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def explore(x, y):
            nonlocal grid, m, n
            if x < 0 or x >= m or y < 0 or y >= n: return
            if grid[x][y] == "0": return
            grid[x][y] = "0" # set as water if explored

            # explore neighbours
            explore(x + 1, y)
            explore(x, y + 1)
            explore(x - 1, y)
            explore(x, y - 1)

        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    explore(row, col)
                    count += 1

        return count
    
