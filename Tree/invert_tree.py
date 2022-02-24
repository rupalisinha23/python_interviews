# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        left_b = self.invertTree(root.left)
        right_b = self.invertTree(root.right)
        
        root.left = right_b
        root.right = left_b
        
        return root
