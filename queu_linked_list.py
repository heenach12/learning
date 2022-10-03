class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def put(self, val):
        new_node = Node(val)
        new_node.next = None
        if (self.size == 0):
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def get(self):
        if self.size == 0:
            return "Queue is empty"
        else:
            self.head = self.head.next
            self.size -= 1
        return self.head

    def peek(self):
        if self.size == 0:
            return "Stack is empty"
        else:
            return self.head.val

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next


l = Queue()
l.put(1)
l.put(2)
l.put(3)
print("first")
l.printList()
print(l.peek())
l.get()
print("after removing")
l.printList()

