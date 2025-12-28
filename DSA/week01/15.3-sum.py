#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        output = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                if threesum == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
        return output
# @lc code=end

