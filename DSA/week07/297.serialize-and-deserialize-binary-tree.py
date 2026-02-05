#
# @lc app=leetcode id=297 lang=python
#
# [297] Serialize and Deserialize Binary Tree
#


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                res.append('N')
                return None
            res.append(str(node.val))
            self.i += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)
        

    def deserialize(self, data):
        vals = data.split(',')
        self.i = 0
        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

