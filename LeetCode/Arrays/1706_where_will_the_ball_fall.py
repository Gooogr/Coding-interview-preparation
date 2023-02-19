# https://leetcode.com/problems/where-will-the-ball-fall

# It's a labirint with different enters and exits. We need to allign all possible
# enters with exits

from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        max_level, enters = len(grid) - 1, len(grid[0]) - 1
        result = []

        def traverse(enter_idx, level, grid):
            val = grid[level][enter_idx]

            # edge cases
            # left dead edge |/
            if enter_idx == 0 and  val == -1:
                return -1
            # right dead edge \|
            if enter_idx == enters and val == 1:
                return -1
            # dead corner \/ ~ [1, -1]
            if val == 1 and grid[level][enter_idx + 1] == -1:
                return -1
            if val == -1 and grid[level][enter_idx - 1] == 1:
                return -1

            # exit
            # +1 - go right, -1 - go left
            if level == max_level:
                return enter_idx + val

            # move right/left
            return traverse(enter_idx + val, level + 1, grid)

        for idx in range(enters + 1):
            result.append(traverse(idx, 0, grid))
            
        return result