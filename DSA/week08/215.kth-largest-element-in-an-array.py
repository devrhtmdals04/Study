#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#
import heapq
# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0] if minHeap else 0
        
# @lc code=end

