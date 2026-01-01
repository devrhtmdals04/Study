#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        column = [[] for _ in range(9)]
        row = [[] for _ in range(9)]
        box = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if not board[i][j].isdigit():
                    continue

                num = int(board[i][j])
                if num in column[j]:
                    return False
                if num in row[i]:
                    return False
                if num in box[(i//3)*3 + (j//3)]:
                    return False
                column[i].append(num)
                row[j].append(num)
                box[(i//3)*3 + (j//3)].append(num)

        return True
# @lc code=end

