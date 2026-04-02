#
# @lc app=leetcode id=304 lang=python
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix(object):

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return
        
        ROWS, COLS = len(matrix), len(matrix[0])
        self.pref = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            for c in range(COLS):
                self.pref[r+1][c+1] = matrix[r][c] + self.pref[r+1][c] + self.pref[r][c+1] - self.pref[r][c]
        

    def sumRegion(self, row1, col1, row2, col2):
        return (self.pref[row2+1][col2+1] - self.pref[row1][col2+1] - self.pref[row2+1][col1] + self.pref[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

