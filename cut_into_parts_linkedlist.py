# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def splitListToParts(self, root: Optional[ListNode], k: int):
      length = 0
      curr = root
      while curr:
          length += 1
          curr = curr.next

      len_mean = length // k
      len_over = length % k

      parts = []
      prev = ListNode(0)
      curr = root

      for _ in range(k):
          if curr:
              parts.append(curr)
              len_part = len_mean + 1 if len_over > 0 else len_mean
              len_over -= 1
              for _ in range(len_part):
                  prev, curr = curr, curr.next
              prev.next = None  # cut here
          else:
              parts.append(None)
      return parts
