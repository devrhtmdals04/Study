#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        len_row = len(matrix[0])
        l, r = 0, len_row * len(matrix) - 1
        while l <= r:
            mid = (l+r) // 2
            col = mid % len_row
            row = mid // len_row
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid +1
        return False
        
# @lc code=end

