#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# hashmap{} = {0= [e, a, t]}, {1, [t, e, a]}

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list)
        for i, s in enumerate(strs):
            sorted_s = "".join(sorted(s))
            hashmap[sorted_s].append(s)
        return list(hashmap.values())
    
#dont use sort

class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list)
        for str in strs:
            alphacount = [0]*26
            for s in str:
                alphacount[ord(s)-ord('a')] += 1
            key = tuple(alphacount)
            hashmap[alphacount].append(str)
        return list(hashmap.values())

# @lc code=end

