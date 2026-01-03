#
# @lc app=leetcode id=424 lang=python
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        mp = {}
        res = 0
        mf = 0
        l = 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            mf = max(mp[s[r]], mf)
            while r - l + 1 - mf > k:
                mp[s[r]] -= 1
                l += 1
            res = max(res, r-1+1)
        return res
# @lc code=end

