#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res
        
class Solution(object):
    def permute(self, nums):
        self.res = []
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, idx):
        if idx == len(nums):
            self.res.append(nums.copy())
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[idx], nums[i]
            self.backtrack(nums, idx+1)
            nums[idx], nums[i] = nums[i], nums[idx]
        
# @lc code=end

