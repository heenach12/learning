class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def middle_element(self):
        slow = self.head
        fast = self.head

        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow.val

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

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next

    def removeNthFromEnd(self, head: Node, n: int):
        temp = Node(0)
        temp.next = head
        head = temp
        count = 0
        while temp:
            count += 1
            temp = temp.next
        temp = head
        count -= n + 1
        while count:
            count -= 1
            temp = temp.next
        temp.next = temp.next.next
        return head.next

l = LinkedList()
l.add_last(3)
l.add_last(4)
l.add_last(6)
l.add_last(8)
l.add_last(9)

l.printList()
print("")
print("kth ", l.middle_element())

l.removeNthFromEnd(l.head, 2)
l.printList()

