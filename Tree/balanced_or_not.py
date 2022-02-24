# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root is None:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        return max(l, r) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        lb = self.isBalanced(root.left)
        rb = self.isBalanced(root.right)
    
        diff = abs(self.height(root.left) - self.height(root.right)) <= 1
    
        if lb & rb & diff:
            return True
        else:
            return False
        
