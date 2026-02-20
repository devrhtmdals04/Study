#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        oldToCopy = {None: None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.val = oldToCopy[cur.val]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        
        cur = head
        while cur:
            new_Node = Node(cur.val)
            new_Node.next = cur.next
            cur.next = new_Node
            cur = new_Node.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        newHead = head.next
        cur = head
        while cur:
            copy = cur.next
            cur.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            cur = cur.next
        return newHead
# @lc code=end

