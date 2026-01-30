#
# @lc app=leetcode id=235 lang=python
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
    
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

        
# @lc code=end

