#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        res = []

        def dfs(i, cur):
            if len(cur) == k:
                res.append(cur.copy())
                return

            if i > n:
                return
            
            cur.append(i)
            dfs(i+1, cur)
            cur.pop()
            dfs(i+1, cur)
            
        dfs(1, [])
        return res
        
# @lc code=end

