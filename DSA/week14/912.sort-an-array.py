#
# @lc app=leetcode id=912 lang=python
#
# [912] Sort an Array
#

# @lc code=start
class Solution(object):
    def sortArray(self, nums):

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            
            return merge(left, right)

        def merge(left, right):
            i = j = 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        
        # Only use small range of val & integer. use [mxVal-mnVal+1] index when arr has negative Value.
        def countingSort(arr):
            mxVal, mnVal = max(arr), min(arr)
            counts = [0] * (mxVal-mnVal+1)
            res = []

            for num in arr:
                counts[num-mnVal] += 1
            
            for i, count in enumerate(counts):
                res.extend([i+mnVal] * count)
            return res
        
        import heapq

        def heapSort(arr):
            heap = []
            for val in arr:
                heapq.heappush(heap, val)
            
            return [heapq.heappop(heap) for _ in range(len(heap))]
            
        return heapSort(nums)
    

        
# @lc code=end

