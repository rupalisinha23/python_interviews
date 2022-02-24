# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root):
        #if root is None return
        result = []
        if root==None:
            return
        #traverse root
        if root.val:
            result.append(root.val)
        else:
            result.append(None)
        #traverse left subtree
        if root.left:
            result.extend(self.preorder(root.left))
        else:
            result.append(None)
        #traverse right subtree
        if root.right:
            result.extend(self.preorder(root.right))
        else:
            result.append(None)
        return result


    def postorder(self, root):
        #if root is None return
        result = []
        if root==None:
            return
        #traverse root
        if root.val:
            result.append(root.val)
        else:
            result.append(None)
        #traverse right subtree
        if root.right:
            result.extend(self.postorder(root.right))
        else:
            result.append(None)
        #traverse left subtree
        if root.left:
            result.extend(self.postorder(root.left))
        else:
            result.append(None)
        return result

    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        elif root.left is None or root.right is None:
            if root.left is None and root.right is None:
                return True
            else:
                return False
        elif self.preorder(root) == self.postorder(root):
            return True
        else:
            return False
