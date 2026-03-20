#
# @lc app=leetcode id=52 lang=python
#
# [52] N-Queens II
#

# @lc code=start
class Solution(object):
    def totalNQueens(self, n):
        col = set()
        posDiag = set()
        negDiag = set()
        res = 0

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        backtrack(0)
        return res
        
# @lc code=end

