#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#
import collections 
# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        mp = collections.defaultdict(int)
        res = 0
        for num in nums:
            mp[num] = mp[num-1] + 1 + mp[num+1]
            mp[num-mp[num-1]] = mp[num]
            mp[num+mp[num+1]] = mp[num]
            res = max(res, mp[num])
        return res


        
# @lc code=end

