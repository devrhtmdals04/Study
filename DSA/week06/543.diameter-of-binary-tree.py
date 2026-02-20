#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = 0
        if not root:
            return 0
        
        def dfs(curr):
            nonlocal res
            left = dfs(curr.left)
            right = dfs(curr.right)

            res = max(res, left+right)
            return 1 + max(left, right)
        
        dfs(root)
        return res

class Solution(object):
    def diameterOfBinaryTree(self, root):
        stack = [root]
        mp = {None: (0,0)}
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            if node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]

                mp[node] = (1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter))

        return mp[root][1]
    
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root: return 0

        stack = [[root,0]]
        heights = {}
        maxDiameter = 0
        while stack:
            node, state = stack[-1]
            if stack == 0: #move left
                stack[-1][1] = 1
                if node.left:
                    stack.append(node.left, 0)
            elif stack == 1: #move right
                stack[-1][1] = 2
                if node.right:
                    stack.append(node.right, 0)
            else: #calculate
                stack.pop()
                left_h = heights.pop(node.left, 0)
                right_h = heights.pop(node.right, 0)

                max_diameter = max(max_diameter, left_h + right_h)
                heights[node] = 1 + max(left_h, right_h)
        return max_diameter
# @lc code=end

