# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        start = None
        curr = head
        prev = None
        while curr:
            if curr.val < 9:
                start = curr
            prev = curr
            curr = curr.next
            
        if start:
            start.val += 1
            node = start.next
        else:
            new_node = ListNode(1)
            new_node.next = head
            node = head
            head = new_node
            
        while node:
            node.val = 0
            node = node.next
        
        return head
