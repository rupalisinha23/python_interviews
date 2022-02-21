# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.data = val
#         self.next = next
def reverse(head):
    ptr_1 = head
    ptr_2 = head.next
    flag = 0
    values = []
    while ptr_1 and ptr_2:
        print(ptr_1.data, ptr_2.data)
        if ptr_1.data % 2 == 0:
            if ptr_2.data % 2 == 0:
                if ptr_2.next is None:
                    values.append(ptr_1.data)
                    values.append(ptr_2.data)
                    values.sort()
                    while ptr_1:
                        ptr_1.data = values.pop()
                        ptr_1 = ptr_1.next
                flag = 1
                values.append(ptr_2.data)
                ptr_2 = ptr_2.next
            else:
                if flag == 1:
                    values.append(ptr_1.data)
                    values.sort()
                    while ptr_1 != ptr_2:
                        ptr_1.data = values.pop()
                        ptr_1 = ptr_1.next
                    flag = 0
                    values = []
                    ptr_2 = ptr_2.next
                else:
                    values.append(ptr_2.data)
                    ptr_2 = ptr_2.next
        else:
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next
    return head
