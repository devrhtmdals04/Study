#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)

            if left == -1 or right == -1:
                return -1

            if abs(left, right) > 1:
                return -1
            return 1 + max(left, right)
        return dfs(root) != -1

class Solution(object):
    def isBlalanced(self, root):
        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1] <= 1)

            return [balanced, 1 + max(left[1]+right[1])]
        return dfs(root)[0]
# @lc code=end

