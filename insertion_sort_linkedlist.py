def insertionSortList(head):
    current = head
    while current is not None:
        temp = current.next
        if temp is not None:
            if temp.data > current.data:
                current.data, temp.data = temp.data, current.data

            if temp.next is not None:
                temp = temp.next
                current = current.next
    return head
