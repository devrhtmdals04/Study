#
# @lc app=leetcode id=698 lang=python
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False
        
        nums.sort(reversed = True)
        target = total // k
        used = [False] * k

        def dfs(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return dfs(0, k-1, 0)
            for j in range(len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                if dfs(i+1, k, subsetSum+nums[j]):
                    return True
                used[j] = False

                if subsetSum == 0:
                    return False
            return False
        return dfs(0, k, 0)

# @lc code=end

