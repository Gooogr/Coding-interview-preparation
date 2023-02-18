# https://leetcode.com/problems/number-of-islands

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows, columns = len(grid), len(grid[0])
        visited = set()
        islands_amount = 0

        #Helper function to find island edges
        def bfs(r, c):
            visited.add((r, c))
            queue = [(r, c)]

            while queue:
                row, column = queue.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = dr + row, dc + column
                    if (r in range(rows) and    # we inside grid limits
                        c in range(columns) and
                        grid[r][c] == '1' and   # in island
                        (r, c) not in visited): # and wasn't where before
                        queue.append((r, c))
                        visited.add((r, c))
            
        for r in range(rows):
            for c in range(columns):
                # if we find new island part - explore it
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands_amount += 1
        return islands_amount