#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q: return True

        elif p and q and q.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        else: return False

class Solution(object):
    def isSameTree(self, p, q):
        stack = [(q, p)]
        res = True
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((p,q))
        return res
# @lc code=end

