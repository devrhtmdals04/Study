#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#
from collections import Counter 
from collections import deque
import heapq 

# @lc code=start
class Solution(object):
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap) + 1
                if task:
                    q.append([task, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])      
        return time
    
# @lc code=end

