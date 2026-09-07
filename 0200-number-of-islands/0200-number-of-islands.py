from typing import List

class Solution:
    def help(self, row, col, max_row, max_col, matrix, visited):
        if row < 0 or col < 0 or row >= max_row or col >= max_col:
            return

        if matrix[row][col] == "0" or visited[row][col]:
            return

        visited[row][col] = True

        self.help(row - 1, col, max_row, max_col, matrix, visited)
        self.help(row + 1, col, max_row, max_col, matrix, visited)
        self.help(row, col - 1, max_row, max_col, matrix, visited)
        self.help(row, col + 1, max_row, max_col, matrix, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        islands = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and not visited[row][col]:
                    islands += 1

                    self.help(row, col, m, n, grid, visited)

        return islands