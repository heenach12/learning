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
        return self.head

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next

    def remove_duplicates(self):
        if not self.head:
            return
        res = LinkedList()
        cur = res.add_last(self.head.val)
        while(self.head):
            if self.head.val != cur.val:
                res.add_last(self.head.val)
                cur = cur.next
            self.head = self.head.next
        # cur = temp = Node(self.head.val)
        # while(self.head):
        #     if self.head.val != cur.val:
        #         cur.next = Node(self.head.val)
        #         cur = cur.next
        #     self.head = self.head.next
        # return temp
        return res


l = LinkedList()
l.add_last(3)
l.add_last(3)
l.add_last(6)
l.add_last(6)
l.add_last(6)
l.add_last(7)


l.printList()
res = l.remove_duplicates()
print("After removing duplicates")

res.printList()
