#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#
from collections import deque
# @lc code=start
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while nums[q[-1]] < nums[r]:
                q.pop()
            q.append(nums[r])

            if l > q[0]:
                q.popleft()
            
            if r+1 >= k:
                res.append(nums[q[0]])
                l+=1
        return res
# @lc code=end

