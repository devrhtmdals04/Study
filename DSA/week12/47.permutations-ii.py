#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        res = []
        nums.sort()

        used = [False] * len(nums)

        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                    continue

                cur.append(nums[i])
                used[i] = True

                dfs(cur)

                cur.pop()
                used[i] = False
        dfs([])
        return res
        
# @lc code=end

