#
# @lc app=leetcode id=51 lang=python
#
# [51] N-Queens
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        res = []
        negDiag = set()
        posDiag = set()
        col = set()
        board = [["."] * n for n in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.apend(copy)
                return
            for c in range(n):
                if c in col or (r - c) in negDiag or (r + c) in posDiag:
                    continue

                col.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                board[r][r] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res
        
# @lc code=end

