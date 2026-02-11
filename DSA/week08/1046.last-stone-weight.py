#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

import heapq
# @lc code=start
class Solution(object):
    def lastStoneWeight(self, stones):
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x, y = heapq.heappop(), heapq.heappop()
            if x != y:
                heapq.heappush(maxHeap, x-y)
                
        return maxHeap[0] if maxHeap else 0
        
# @lc code=end

