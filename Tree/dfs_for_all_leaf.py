# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        result = []
        stack = [(root, "")]
        while stack:
            curr, temp = stack.pop()
            temp = temp + str(curr.val)
            if not curr.right and not curr.left:
                result.append(temp)
            if curr.left:
                stack.append((curr.left, temp + "->"))
            if curr.right:
                stack.append((curr.right, temp + "->"))
        return result
            
