# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self,node):
        leftMax = 0
        if node.left:
            leftMax = self.help(node.left)+1
        rightMax = 0
        if node.right:
            rightMax = self.help(node.right)+1
        self.ans = max(self.ans, leftMax + rightMax)
        return max(leftMax,rightMax)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans=0
        self.help(root)
        return self.ans

        