#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        res = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            res = max(res + node.val + left + right)
            return node.val + max(left, right)
        
# @lc code=end

