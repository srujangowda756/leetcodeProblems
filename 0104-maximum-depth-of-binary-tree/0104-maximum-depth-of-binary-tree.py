# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self,node):
        if not node:
            return 0
        print(node.val)
        left=self.help(node.left)+1
        right=self.help(node.right)+1
        return max(left,right)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left=self.help(root.left)
        right=self.help(root.right)
        return max(left,right)+1

        
        