"""
Make numbers of inversed Linked Lists and the numbers and convert to another LinkedList after inverting
Status: Solved by Me
"""


class ListNode:
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


def reverse_string(input):
    return input[::-1]


def get_number(input: ListNode):
    input_string = ''
    while input is not None:
        input_string += str(input.val)
        input = input.next
    return reverse_string(input_string)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_string = get_number(l1)
        l2_string = get_number(l2)
        sum = int(l1_string) + int(l2_string)
        reverse_sum = reverse_string(str(sum))
        nodes = len(reverse_sum)
        node_list = []
        for i in range(0, nodes):
            node_list.append(ListNode(int(reverse_sum[i])))
        count = 0
        while count+1 != nodes:
            node_list[count].next = node_list[count+1]
            count += 1
        return node_list[0]


if __name__ == '__main__':
    l1 = ListNode(5)
    l2 = ListNode(0)
    l3 = ListNode(6)
    l1.next = l2
    l2.next = l3
    p1 = ListNode(8)
    p2 = ListNode(0)
    p3 = ListNode(9)
    p1.next = p2
    p2.next = p3
    solution = Solution()
    print(solution.addTwoNumbers(l1, p1).traverse())