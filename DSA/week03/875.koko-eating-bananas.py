#
# @lc app=leetcode id=875 lang=python
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            mid = (l+r)//2
            total = 0
            for p in piles:
                total += (p + mid -1) // mid
            if total <= h:
                r = mid -1
                res = mid
            else:
                l = mid + 1
        return res
        
# @lc code=end

