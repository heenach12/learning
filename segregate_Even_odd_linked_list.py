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


def segregate_even_odd(head):
        even_start = None
        even_end = None
        odd_start = None
        odd_end = None

        cur = head
        while(cur != None):
            if cur.val % 2 == 0:
                if even_start == None:
                    even_start = cur
                    even_end = even_start
                else:
                    even_end.next = cur
                    even_end = even_end.next
            else:
                if odd_start == None:
                    odd_start = cur
                    odd_end = odd_start
                else:
                    odd_end.next = cur
                    odd_end = odd_end.next
            cur = cur.next

        if odd_start == None or even_start == None:
            return

        even_end.next = odd_start
        odd_end.next = None
        head = even_start
        return head

l = LinkedList()
l.add_last(3)
l.add_last(4)
l.add_last(5)
l.add_last(8)

l.printList(l.head)

print("segregate")
g = segregate_even_odd(l.head)
l.printList(g)


