#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        res = set()
        def backtrack(i, cur):
            if i == len(nums):
                res.add(tuple(cur))
                return 
            
            cur.append(nums[i])
            backtrack(i+1, cur)
            cur.pop()
            backtrack(i+1, cur)

        nums.sort()
        backtrack(0, [])
        return [list(s) for s in res]

class Solution(object):
    def subsestWithDup(self, nums):
        res = []
        nums.sort()
        def backtrack(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            backtrack(i+1, cur)
            cur.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, cur)
        backtrack(0, [])
        return res
# @lc code=end

