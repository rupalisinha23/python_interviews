# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def range_sum_bst(root: TreeNode, l: int, r: int) -> int:
    """
    return sum within a given range out of a binary search tree
    :param root:
    :param l:
    :param r:
    :return:
    """
    if root is None:
        return 0
    if l <= root.val <= r:
        return root.val + range_sum_bst(root.left, l, r) + range_sum_bst(root.right, l, r)
    return 0 + range_sum_bst(root.left, l, r) + range_sum_bst(root.right, l, r)


m = TreeNode(10)
m.left = TreeNode(5)
m.right = TreeNode(15)
m.left.left = TreeNode(3)
m.left.right = TreeNode(7)
m.left.right.left = None
m.left.right.right = TreeNode(18)

print(range_sum_bst(m, 7, 15))