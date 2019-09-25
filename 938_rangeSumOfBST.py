# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        if root.val <= R and root.val >= L:
            res+=root.val
            res+=self.rangeSumBST(root.left,L,R)
            res+=self.rangeSumBST(root.right,L,R)
        if root.val > R:
            res+=self.rangeSumBST(root.left,L,R)
        if root.val < L:
            res+=self.rangeSumBST(root.right,L,R)
        return res