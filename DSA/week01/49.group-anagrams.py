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
        hashmap = {}
        output = []
        for i, s in enumerate(strs):
            for a in s:
                if a not in hashmap:
                    continue
            output.append(s)
        return output
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
# @lc code=end

