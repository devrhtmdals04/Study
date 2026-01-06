#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        mp = {}
        l = 0
        for r in range(s):
            if s[r] in mp:
                l =  max(mp[s[r]]+1, l)
            mp[s[r]] = r
            res = max(r-l+1, res)
        return max
        
# @lc code=end

