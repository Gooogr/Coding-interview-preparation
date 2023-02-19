# https://leetcode.com/problems/spiral-matrix/

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # or we can track visited nodes in set(). But it costs memory
        while left < right and top < bottom:
            # go right
            for idx in range(left, right):
                result.append(matrix[top][idx])
            top += 1
            # go down
            for idx in range(top, bottom):
                result.append(matrix[idx][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # go left
            for idx in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][idx])
            bottom -= 1
            # go up
            for idx in range(bottom - 1, top - 1, -1):
                result.append(matrix[idx][left])
            left += 1
        return result