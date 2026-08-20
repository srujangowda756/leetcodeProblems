# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def help(self,root,p,q):
        if not root:
            return None

        if root==p or root==q:
            return root

        leftAns=self.help(root.left,p,q)
        rightAns=self.help(root.right,p,q)

        if leftAns and rightAns:
            return root
        if leftAns:
            return leftAns
        return rightAns
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p==root or q==root:
            return root
        return self.help(root,p,q)
        
        
        