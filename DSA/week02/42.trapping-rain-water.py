#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
#two-pointer
class Solution(object):
    def trap(self, height):
        l, r = 0, len(height)-1
        ml, mr = height[l], height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                ml = max(ml, height[l])
                res += ml - height[l]
                l+=1
            else:
                mr = max(mr, height[r])
                res += mr - height[r]
                r-=1
        return res

#stack
class Solution(object):
    def trap(self, height):
        stack = []
        res = 0
        for r in range(len(height)):
            while stack and height[stack[-1]] < height[r]:
                bottom = stack.pop()
                if not stack:
                    break
                l = stack[-1]
                width = r-l-1
                h = min(height[r], height[l]) - height[bottom]
                res += width*h
            stack.append(r)          
        return res
# @lc code=end

