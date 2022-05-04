# https://leetcode.com/problems/valid-sudoku/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Create hashmaps for columns, rows, and subsquares
        # defaultdict is more convenient because it automatically adds new keys
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue
                if (value in rows[r] or
                    value in cols[c] or
                    value in squares[f'{r//3}{c//3}']):
                    return False
                rows[r].add(value)
                cols[c].add(value)
                squares[f'{r//3}{c//3}'].add(value)
        return True
