# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def range_sum_bst(root: TreeNode, L: int, R: int) -> int:
    if root is None:
        return 0
    if L <= root.val <= R:
        return root.val + range_sum_bst(root.left, L, R) + range_sum_bst(root.right, L, R)
    return 0 + range_sum_bst(root.left, L, R) + range_sum_bst(root.right, L, R)


m = TreeNode(10)
m.left = TreeNode(5)
m.right = TreeNode(15)
m.left.left = TreeNode(3)
m.left.right = TreeNode(7)
m.left.right.left = None
m.left.right.right = TreeNode(18)

print(range_sum_bst(m, 7, 15))