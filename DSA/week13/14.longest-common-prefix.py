#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        res = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < min(len(res), len(strs[i])):
                if res[j] != strs[i][j]:
                    break
                j += 1
            res = res[:j]
        return res

class Solution(object):
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return strs[0][:i]
        return strs[0]            
# @lc code=end

