#
# @lc app=leetcode id=572 lang=python
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val == subRoot.val:
                if self.checkSame(node, subRoot):
                    return True

            stack.append(node.left)
            stack.append(node.right)
        return False
    
    def checkSame(self, p, q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.checkSame(p.left, q.left) and self.checkSame(p.right, q.right)
        else:
            return False
# @lc code=end

