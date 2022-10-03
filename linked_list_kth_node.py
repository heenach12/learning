class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def k_th_element_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while(fast != None):
            slow = slow.next
            fast = fast.next
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

l = LinkedList()
l.add_last(3)
l.add_last(4)
l.add_last(6)
l.add_last(8)

l.printList()
print("")
print("kth ", l.k_th_element_from_last(2))
