class Solution(object):
    def twoSum(self, nums, target):
       hashmap = {}
       for inputindex, n in enumerate(nums):
           diff = target - n
           if n in hashmap:
               return [hashmap[diff], inputindex]
           hashmap[diff] = inputindex
            


