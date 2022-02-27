# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None and list2 is not None:
            return list2
        
        if list2 is None and list1 is not None:
            return list1
        head1 = list1
        head2 = list2
        curr = ListNode()
        head = curr
        is_first = True

        while head1 is not None and head2 is not None:
            if is_first is False:
                curr.next = ListNode()
                curr = curr.next
            if head1.val <= head2.val:
                curr.val = head1.val
                head1 = head1.next
            else:
                curr.val = head2.val
                head2 = head2.next
            is_first = False
        
        if head2 is not None:
            curr.next = head2
            head2 = head2.next
            
        if head1 is not None:
            curr.next = head1
            head1 = head1.next
            
        return head
