class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_last(self, val):
        temp = Node(val)
        temp.next = None
        if self.size == 0:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

        self.size += 1

    def printList(self, head):
        temp = head
        while(temp != None):
            print(temp.val, end=" ")
            temp = temp.next


def rearrange_even_odd(head):
    if not head or not head.next or not head.next.next:
        return head
    odd = head
    even = head.next
    even_first = head.next

    while(odd and even):
        odd.next = even.next
        if odd.next:
            odd = odd.next
            even.next = odd.next
            even = even.next
        else:
            break

    odd.next = even_first
    return head
