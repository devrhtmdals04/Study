#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        half = (len(A) + len(B)) // 2
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            leftA = A[i] if A[i] >= 0 else float("-infinity")
            rightA = A[i+1] if i+1 < len(A) else float("infinity")
            leftB = B[j] if B[j] >= 0 else float("-infinity")
            rightB = B[j+1] if j+1 < len(B) else float("infinity")

            if leftA <= rightB and leftB <= rightA:
                if (len(A)+len(B)) % 2:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                
            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1

        
# @lc code=end

