#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, index = stack[-1].pop()
                res[index] = i-index
            stack.append((t, i))
        return res

class Solution(object):
    def dailyTempertaures(self, temperatures):
        length = len(temperatures)
        res = [0] * length
        for i in range(length-2, -1, -1):
            j = i + 1
            while j < length and temperatures[j] <= temperatures(i):
                if res[j] == 0:
                    j = length
                    break
                j += res[j]
            res[i] = j-i
        return res
                
# @lc code=end

