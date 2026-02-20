#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

import heapq
# @lc code=start
class Solution(object):
    def kClosest(self, points, k):
        maxHeap = []
        for point in points:
            x, y = point[0], point[1]
            dist = x**2 + y**2
            heapq.heappush(maxHeap, [-dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [[x, y] for dist, x, y in maxHeap]
# @lc code=end

