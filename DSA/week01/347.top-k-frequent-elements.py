#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        hash = {}
        for i, num in enumerate(nums):
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        sortedhash = sorted(hash.items(), key=lambda x:x[1], reverse=True)
        output = []
        for i in range(k):
            output.append(sortedhash[i][0])
        return output

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        top_k = Counter(nums).most_common(k)
        return [item[0] for item in top_k]
    
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        return heapq.nlargest(k, count.keys(), key=count.get)
        
        
# @lc code=end

