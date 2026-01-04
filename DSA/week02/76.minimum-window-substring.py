#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        count, window = {}, {}
        res, minres = [-1,-1], float('inf')
        if t == "":
            return ""
        for c in t:
           count[c] = count.get(c, 0) + 1

        need = len(count)
        for r in range(len(s)):
            window[s[r]] = window.get([s[r]], 0) + 1
            if s[r] in count and window[s[r]] == count[s[r]]:
               have += 1
            
            while have == need:
                if r-l+1 < minres:
                    minres = r-l+1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] == count[s[l]]:
                    have -= 1
                l+=1

        l, r = res
        return s[l:r+1] if minres != float("inf") else ""
# @lc code=end

