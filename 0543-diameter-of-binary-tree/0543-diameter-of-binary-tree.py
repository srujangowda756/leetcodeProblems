# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans=0
        def help(node):
            leftMax = 0
            if node.left:
                leftMax = help(node.left)+1
            rightMax = 0
            if node.right:
                rightMax = help(node.right)+1
            nonlocal ans
            ans = max(ans, leftMax + rightMax)
            return max(leftMax,rightMax)
        help(root)
        return ans

        