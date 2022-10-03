def decimal_equivalent(head):
    res = 0
    while(head):
        res = (res<<1)+head.data
        head = head.next
    return res
