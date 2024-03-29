# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 617

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1: 
            return t2
        if not t2: 
            return t1
        newT = TreeNode(t1.val+t2.val)
        newT.right = self.mergeTrees(t1.right, t2.right)
        newT.left = self.mergeTrees(t1.left, t2.left)
        return newT