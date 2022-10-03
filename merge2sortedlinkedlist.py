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

    def merge_sort(self, l1, l2):
        first = l1.head
        sec = l2.head

        result = LinkedList()
        while(first != None and sec != None):
            if first.val < sec.val:
                result.add_last(val=first.val)
                first = first.next
            else:
                result.add_last(val=sec.val)
                sec = sec.next

        while(first != None):
            result.add_last(first.val)
            first = first.next

        while(sec != None):
            result.add_last(sec.val)
            sec = sec.next
        return result




l = LinkedList()
l.add_last(3)
l.add_last(4)
l.add_last(6)
l.add_last(8)
l.add_last(9)


l.printList()

l2 = LinkedList()
l2.add_last(12)
l2.add_last(16)
l2.add_last(18)
l2.add_last(20)
l2.add_last(30)
l2.add_last(45)
l2.add_last(75)
print("")
l2.printList()

res = l.merge_sort(l, l2)
print("after merging")
res.printList()


