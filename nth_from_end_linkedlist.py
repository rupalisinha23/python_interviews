class ListNode:
    """
    Nth node value from the end of a linked list
    Status: Solved by Me
    """
    def __init__(self, x):
        self.val = x
        self.next = None

    def traverse(self):
        node = self  # start from the head node
        visual = ''
        while node is not None:
            visual += str(node.val) + '->'
            node = node.next
        visual += 'NULL'
        return visual

    def nth_from_end(self, n):
        node_right = self
        node_left = self
        for i in range(0, n):
            if node_right is None:
                return None
            node_right = node_right.next
        while node_right is not None:
            node_right = node_right.next
            node_left = node_left.next
        return node_left


if __name__ == '__main__':
    l1 = ListNode(5)
    l2 = ListNode(0)
    l3 = ListNode(6)
    l4 = ListNode(7)
    l5 = ListNode(8)
    l6 = ListNode(9)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = None
    print(l1.traverse())
    node_n_end = l1.nth_from_end(3)
    if node_n_end is None:
        print('The linked list is not long enough')
    else:
        print(str(node_n_end.val))
