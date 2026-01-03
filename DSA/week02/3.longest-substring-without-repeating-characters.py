#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        mp = []
        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[r]+1, l)
            mp[s[r]] = r
            res = max(res, r-1+1)
        
# @lc code=end

