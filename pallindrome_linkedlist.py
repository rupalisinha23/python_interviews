# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return True

        fast = head
        slow = head
        prev = None
        flag = 1

        while fast and fast.next:
            if not fast.next.next:
                flag = 0
                break
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp

        fast = slow.next
        slow.next = prev
        
        # if odd
        if flag:
            slow = slow.next
      
        while fast and slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next

        return True
            
        
