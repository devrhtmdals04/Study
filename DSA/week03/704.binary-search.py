#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#
import bisect
# @lc code=start
class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return -1
    
    
class Solution(object):
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target):
        return index if index < len(nums) and nums[index] == target else -1
        
# @lc code=end

