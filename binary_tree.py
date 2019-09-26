class Node:
    """
    Completeness of a binary tree
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

    # This function checks if a binary tree is complete or not
    def is_complete(self, root, index, number_nodes):
        # An empty tree is complete
        if root is None:
            return True

        # If index assigned to current nodes is more than number of
        # nodes in tree, then tree is not complete
        if index >= number_nodes:
            return False

        # Recur for left and right sub tress
        return self.is_complete(root.left, 2 * index + 1, number_nodes)\
               and self.is_complete(root.right, 2 * index + 2,
                                    number_nodes)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    node_count = root.count_nodes(root)
    index = 0
    print("{} nodes are present in this tree".format(str(node_count)))
    if root.is_complete(root, index, node_count):
        print("The Binary Tree is complete")
    else:
        print("The Binary Tree is not complete")
