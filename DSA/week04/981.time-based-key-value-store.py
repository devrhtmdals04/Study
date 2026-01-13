#
# @lc app=leetcode id=981 lang=python
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap(object):

    def __init__(self):
        keyStore = {}
    def set(self, key, value, timestamp):
        self.keyStore.setdefault(key, []).append([value,timestamp])

    def get(self, key, timestamp):
        res, values = "", self.keyStore.get[key,[]]
        l, r = 0, len(values) - 1
        while l<=r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

