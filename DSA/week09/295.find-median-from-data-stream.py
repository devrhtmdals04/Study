#
# @lc app=leetcode id=295 lang=python
#
# [295] Find Median from Data Stream
#
import heapq
# @lc code=start
class MedianFinder(object):

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        heapq.heappush(self.maxHeap, -num)

        if self.maxHeap and self.minHeap and-self.maxHeap[0] > self.minHeap[0]:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        
        if len(self.maxHeap) < len(self.minHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

    def findMedian(self):
        if len(self.maxHeap) - len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap(self.minHeap)) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

