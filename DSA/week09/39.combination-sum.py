#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def dfs(i, total, cur):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return       
                cur.append(candidates[j])
                dfs(i, total, cur)
                cur.pop()

        dfs(0, 0, [])
        return res
        
# @lc code=end

