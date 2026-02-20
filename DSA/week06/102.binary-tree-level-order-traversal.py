#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        res = []
        def dfs(node, floor):
            if not node: return None
            if len(res) == floor:
                res.append([])
            res[floor].append(node)
            dfs(node.left, floor + 1)
            dfs(node.right, floor + 1)
        dfs(root, 0)
        return res

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        q = deque()
        q.append(root)
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
# @lc code=end

