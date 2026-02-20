#
# @lc app=leetcode id=1448 lang=python
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        res = 0
        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res
        return dfs(root, root.val)

from collections import deque
class Solution(object):
    def goodNodes(self, root):
        q = deque()
        q.append([root, -float('inf')])
        res = 0

        while q:
            node, maxVal = q.popleft()
            if node.val >= maxVal:
                res += 1
            if node.left:
                q.append([node.left, max(node.val, maxVal)])
            if node.right:
                q.append([node.right, max(node.val, maxVal)])
        return res
# @lc code=end

