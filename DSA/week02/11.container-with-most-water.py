#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, heights):
        maxarea = -1
        left, right = 0, len(heights) - 1 
        while left < right:
            height = min(heights[left], heights[right])
            floor = right - left
            area = height * floor
            maxarea = max(maxarea, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right += 1
        return maxarea

# @lc code=end

