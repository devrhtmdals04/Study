#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
from collections import defaultdict
# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        return max(count, key=count.get)

#Boyer--Morore Voting Algorithm
class Solution(object):
    def majorityElement(self, nums):
        res = None
        count = 0
        for num in nums:
            if count == 0:
                res = num
            if res == num:
                count += 1
            else:
                count -= 1
        return res
        
# @lc code=end

