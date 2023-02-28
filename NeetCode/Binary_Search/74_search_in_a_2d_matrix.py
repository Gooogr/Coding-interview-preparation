# https://leetcode.com/problems/search-a-2d-matrix

from typing import List

# Not so bright approach - convert 2D list to 1D list
# and use standart binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #flatten matrix
        arr = sum(matrix, [])
        # search value as usual binary search
        l, r = 0, len(arr) - 1
        while l <= r:
            middle = (l + r) // 2
            if arr[middle] == target:
                return True
            elif arr[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False
    
# Fancy approach with 2D indexing
# row_idx = idx // columns_amount
# column_idx = idx % columns_amount

# 0, 1, 2, 3
# 4, 5, 6, 7
# 8, 9, 10, 11

# n_columns = 4
# idx = 9

# row_idx = 10 // 4 = 2
# column_idx = 10 % 4 = 1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, clmns = len(matrix), len(matrix[0])
        l, r = 0, rows * clmns - 1
        while l <= r:
            middle = (l + r) // 2
            value = matrix[middle // clmns][middle % clmns]
            if value == target:
                return True
            elif value < target:
                l = middle + 1
            else:
                r = middle - 1
        return False