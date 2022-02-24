# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root==None:
            return
        #traverse root
        if root.val is not None:
            result.append(root.val)
        #traverse left subtree
        if root.left:
            result.extend(self.preorderTraversal(root.left))
        #traverse right subtree
        if root.right:
            result.extend(self.preorderTraversal(root.right))
        return result
      
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root==None:
            return

        #traverse left subtree
        if root.left:
            result.extend(self.postorderTraversal(root.left))

        #traverse right subtree
        if root.right:
            result.extend(self.postorderTraversal(root.right))

        #traverse root
        if root.val is not None:
            result.append(root.val)

        return result
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if root is None:
            return
        
        #traverse left subtree
        if root.left:
            result.extend(self.inorderTraversal(root.left))
            
        #traverse root
        if root.val is not None:
            result.append(root.val)
            
        #traverse right subtree
        if root.right:
            result.extend(self.inorderTraversal(root.right))
        
        return result
