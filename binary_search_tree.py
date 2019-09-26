class Node:
    """
    Binary Search Tree or not
    """
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # This function counts the number of nodes in a binary tree
    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + \
                   self.count_nodes(root.right)

    # This function checks if a binary tree is binary search tree or not
    def is_bst(self, root, lower_lim, upper_lim):

        # An empty tree is complete
        if lower_lim is not None and root.key < lower_lim:
            return False
        if upper_lim is not None and root.key > upper_lim:
            return False

        is_left_bst = True
        is_right_bst = True

        if root.left:
            is_left_bst = self.is_bst(root.left, lower_lim, root.key)

        if is_left_bst and root.right:
            is_right_bst = self.is_bst(root.right, root.key, upper_lim)

        return is_left_bst and is_right_bst


if __name__ == '__main__':
    root = Node(3)
    root.left = Node(1)
    root.right = Node(5)
    root.left.left = Node(0)
    root.left.right = Node(2)
    root.right.left = Node(4)
    root.right.right = Node(6)

    node_count = root.count_nodes(root)
    index = 0
    print("{} nodes are present in this tree".format(str(node_count)))
    if root.is_bst(root, None, None):
        print("The Binary Tree is Binary Search Tree")
    else:
        print("The Binary Tree is not a Binary Search Tree")
